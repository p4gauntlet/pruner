#include <fstream>
#include <iostream>
#include <random>
#include <sys/stat.h>

#include "contrib/json.h"
#include "frontends/common/parseInput.h"
#include "ir/ir.h"

#include "boolean_pass.h"
#include "compiler_pruner.h"
#include "expression_pruner.h"
#include "pruner_options.h"
#include "pruner_util.h"
#include "statement_pruner.h"

const IR::P4Program *prune(const IR::P4Program *program,
                           P4PRUNER::PrunerOptions options, int req_exit_code) {
    program = P4PRUNER::prune_statements(program, options, req_exit_code);
    program = P4PRUNER::prune_expressions(program, options, req_exit_code);
    program = P4PRUNER::prune_bool_expressions(program, options, req_exit_code);
    program = P4PRUNER::apply_compiler_passes(program, options, req_exit_code);
    return program;
}

void process_seed(P4PRUNER::PrunerOptions options) {
    uint64_t seed;
    if (options.seed) {
        std::cerr << "Using provided seed.\n";
        try {
            seed = boost::lexical_cast<uint64_t>(options.seed);
        } catch (boost::bad_lexical_cast &) {
            ::error("invalid seed %s", options.seed);
            exit(EXIT_FAILURE);
        }
    } else {
        // no seed provided, we generate our own
        std::cerr << "Using generated seed.\n";
        std::random_device r;
        seed = r();
    }
    std::cerr << "Seed:" << seed << "\n";
    P4PRUNER::set_seed(seed);
}

int main(int argc, char *const argv[]) {
    AutoCompileContext autoP4toZ3Context(new P4PRUNER::P4PrunerContext);
    auto &options = P4PRUNER::P4PrunerContext::get().options();
    options.langVersion = CompilerOptions::FrontendVersion::P4_16;
    const IR::P4Program *program;

    if (options.process(argc, argv) != nullptr) {
        options.setInputFile();
    }
    if (::errorCount() > 0)
        exit(EXIT_FAILURE);

    if (options.file == nullptr) {
        options.usage();
        exit(EXIT_FAILURE);
    }
    P4PRUNER::set_stripped_program_name(options.file);

    P4PRUNER::PrunerConfig pruner_conf;

    if (options.config_file) {
        std::ifstream config_file(options.config_file);
        nlohmann::json config_json;
        config_file >> config_json;
        pruner_conf.exit_code = config_json.at("exit_code");
        pruner_conf.compiler = cstring(config_json.at("compiler"));
        pruner_conf.validation_bin = cstring(config_json.at("validation_bin"));
        pruner_conf.prog_before = cstring(config_json.at("prog_before"));
        pruner_conf.prog_post = cstring(config_json.at("prog_after"));

    } else if (options.validator_script) {
        // Retrieve the exit code from the unchanged program
        struct stat buffer;
        INFO("Checking " << options.file);
        if (stat(options.validator_script, &buffer) != 0) {
            ::error("Validator Binary %s does not exist! Exiting.",
                    options.validator_script);
            return EXIT_FAILURE;
        }
        pruner_conf.exit_code =
            P4PRUNER::get_exit_code(options.file, options.validator_script);
        INFO("Got code : " << pruner_conf.exit_code << " for the main file");

    } else {
        ::error("Need to provide either a validator_script or a config file!");
        options.usage();
        return EXIT_FAILURE;
    }

    process_seed(options);

    // parse the input P4 program
    program = P4::parseP4File(options);
    auto original = program;

    if (program != nullptr && ::errorCount() == 0) {
        program = prune(program, options, pruner_conf.exit_code);
        if (options.print_pruned) {
            P4PRUNER::print_p4_program(program);
        }
        // if the emit flag is enabled, also emit the new P4 program
        if (options.emit_p4) {
            P4PRUNER::emit_p4_program(program, STRIPPED_NAME);
        }
        INFO("Total reduction percentage = "
             << P4PRUNER::measure_pct(original, program) << " %");
    }

    return ::errorCount() > 0;
}
