#include "frontends/common/parseInput.h"
#include "ir/ir.h"


#include "compiler_pruner.h"
#include "pruner_options.h"
#include "pruner_util.h"
#include "statement_pruner.h"

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

    INFO("Checking " << options.file);

    // Retrieve the exit code from the unchanged program
    int required_exit_code = get_exit_code(options.file, options);
    INFO("Got code : " << required_exit_code << " for the main file");

    // parse the input P4 program
    program = P4::parseP4File(options);

    if (program != nullptr && ::errorCount() == 0) {
        program =
            P4PRUNER::prune_statements(program, options, required_exit_code);
        program = P4PRUNER::apply_compiler_passes(program, options,
                                                  required_exit_code);
        if (options.print_pruned) {
            P4PRUNER::print_p4_program(program);
        }
        // if the emit flag is enabled, also emit the new P4 program
        if (options.emit_p4) {
            P4PRUNER::emit_p4_program(program, STRIPPED_NAME);
        }
    }

    return ::errorCount() > 0;
}
