
#include <fstream>
#include <iostream>
#include <random>

#include "contrib/json.h"
#include "frontends/common/parseInput.h"
#include "ir/ir.h"

#include "boolean_pruner.h"
#include "compiler_pruner.h"
#include "expression_pruner.h"
#include "pruner_options.h"
#include "pruner_util.h"
#include "replace_variables.h"
#include "statement_pruner.h"
const IR::P4Program *prune(const IR::P4Program *program,
                           P4PRUNER::PrunerConfig pruner_conf) {
    // program = P4PRUNER::prune_statements(program, pruner_conf);
    // program = P4PRUNER::prune_expressions(program, pruner_conf);
    // program = P4PRUNER::prune_bool_expressions(program, pruner_conf);
    // program = P4PRUNER::apply_compiler_passes(program, pruner_conf);
    program = P4PRUNER::replace_variables(program, pruner_conf);
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

P4PRUNER::PrunerConfig get_config(P4PRUNER::PrunerOptions options) {
    if (!P4PRUNER::file_exists(options.config_file)) {
        ::error("Config file %s does not exist! Exiting.", options.config_file);
        exit(EXIT_FAILURE);
    }
    P4PRUNER::PrunerConfig pruner_conf;
    nlohmann::json config_json;

    std::ifstream config_file(options.config_file);
    config_file >> config_json;

    pruner_conf.exit_code = config_json.at("exit_code");
    pruner_conf.compiler = cstring(config_json.at("compiler"));
    pruner_conf.validation_bin = cstring(config_json.at("validation_bin"));
    pruner_conf.prog_before = cstring(config_json.at("prog_before"));
    pruner_conf.prog_post = cstring(config_json.at("prog_after"));
    pruner_conf.working_dir = options.working_dir;
    pruner_conf.allow_undef = config_json.at("allow_undef");
    // also store the new output name
    // TODO(fruffy): Make this an ;option
    cstring output_name = P4PRUNER::remove_extension(options.file);
    output_name += "_stripped.p4";
    pruner_conf.out_file_name = output_name;
    return pruner_conf;
}

P4PRUNER::PrunerConfig get_config_from_script(P4PRUNER::PrunerOptions options) {
    INFO("Grabbing config by using the validation script.");
    if (!P4PRUNER::file_exists(options.validation_bin)) {
        ::error("Validator Binary %s does not exist! Exiting.",
                options.validation_bin);
        exit(EXIT_FAILURE);
    }

    // assemble the command to run the validation script to get a config file
    cstring command = "python3 ";
    command += options.validation_bin;
    command += " -i ";
    command += options.file;
    // suppress output
    command += " -ll CRITICAL ";
    // change the output dir
    command += " -o ";
    command += options.working_dir;
    // also toggle config recording
    command += " -d ";
    int ret = system(command);
    if (ret == 0) {
        ::warning("There was no error. Pruning will yield bogus results.");
    }

    cstring file_stem = P4PRUNER::get_file_stem(options.file);
    // assemble the path for the config file
    // this is not great but we have no other way right now
    cstring config_file = realpath(options.working_dir, nullptr);
    config_file += "/";
    config_file += file_stem;
    config_file += "/";
    config_file += file_stem;
    config_file += "_info.json";
    options.config_file = config_file;
    return get_config(options);
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

    if (P4PRUNER::file_exists(options.working_dir)) {
        ::error("Working directory already exists. To be safe, please choose a "
                "non-existent directory.");
        return EXIT_FAILURE;
    }

    P4PRUNER::PrunerConfig pruner_conf;

    if (options.config_file) {
        pruner_conf = get_config(options);
    } else if (options.validation_bin) {
        pruner_conf = get_config_from_script(options);
    } else {
        ::error("Need to provide either a validation_bin or a config file!");
        options.usage();
        return EXIT_FAILURE;
    }
    // if a seed was provided, use it
    // otherwise generate a random seed and set it
    process_seed(options);
    // parse the input P4 program
    program = P4::parseP4File(options);

    if (program != nullptr && ::errorCount() == 0) {
        auto original = program;
        program = prune(program, pruner_conf);
        if (options.print_pruned) {
            P4PRUNER::print_p4_program(program);
        }
        // if the emit flag is enabled, also emit the new P4 program
        if (options.emit_p4) {
            P4PRUNER::emit_p4_program(program, pruner_conf.out_file_name);
        }
        INFO("Total reduction percentage = "
             << P4PRUNER::measure_pct(original, program) << " %");
    }
    INFO("Done. Removing ephemeral working directory.");
    P4PRUNER::remove_file(pruner_conf.working_dir);
    return ::errorCount() > 0;
}
