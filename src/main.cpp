#include <sys/stat.h>

#include <random>

#include "frontends/common/parseInput.h"
#include "ir/ir.h"

#include "boolean_pass.h"
#include "compiler_pruner.h"
#include "expression_pruner.h"
#include "pruner_options.h"
#include "pruner_util.h"
#include "statement_pruner.h"

const IR::P4Program *prune(const IR::P4Program *program,
                                   P4PRUNER::PrunerOptions options,
                                   int req_exit_code) {
    program = P4PRUNER::prune_statements(program, options, req_exit_code);
    program = P4PRUNER::prune_expressions(program, options, req_exit_code);
    program = P4PRUNER::prune_bool_expressions(program, options, req_exit_code);
    program = P4PRUNER::apply_compiler_passes(program, options, req_exit_code);
    return program;
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
        return 1;

    if (options.file == nullptr || options.validator_script == nullptr) {
        options.usage();
        return 1;
    }
    P4PRUNER::set_stripped_program_name(options.file);

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

    INFO("Checking " << options.file);

    // Retrieve the exit code from the unchanged program
    struct stat buffer;
    if (stat(options.validator_script, &buffer) != 0) {
        ::error("Validator Binary %s does not exist! Exiting.",
                options.validator_script);
        return EXIT_FAILURE;
    }
    int req_exit_code =
        P4PRUNER::get_exit_code(options.file, options.validator_script);
    INFO("Got code : " << req_exit_code << " for the main file");

    // parse the input P4 program
    program = P4::parseP4File(options);
    auto original = program;

    if (program != nullptr && ::errorCount() == 0) {
        program = prune(program, options, req_exit_code);
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
