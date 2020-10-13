#define PRUNE_STMT_MAX 100
#define PRUNE_ITERS 50

#include <fstream>

#include "frontends/common/parseInput.h"
#include "frontends/p4/toP4/toP4.h"
#include "ir/ir.h"
#include "lib/cstring.h"
#include "lib/log.h"
#include "lib/nullstream.h"

#include "libgen.h"
#include "pruner.h"
#include "pruneroptions.h"
#include "unistd.h"

cstring remove_extension(cstring filename) {
    // find the last dot
    const char *last_dot = filename.findlast('.');
    // there is no dot in this string, just return the full name
    if (not last_dot) {
        return filename;
    }
    // otherwise get the index, remove the dot
    size_t idx = (size_t)(last_dot - filename);
    return filename.substr(0, idx);
}

const std::vector<const IR::Statement *>
collect_statements(const IR::P4Program *temp, int max) {
    // An inspector that collects some statements at random
    P4PRUNER::Collector *collector = new P4PRUNER::Collector(max);
    temp->apply(*collector);
    return collector->to_prune;
}

const IR::P4Program *prune_statements(const IR::P4Program *program,
                                      P4PRUNER::PrunerOptions options,
                                      int required_exit_code) {
    cstring stripped_name = remove_extension(options.file);
    stripped_name += "_stripped.p4";
    int same_before_pruning = 0;
    int max_statements = PRUNE_STMT_MAX;
    cstring new_command = "python3 ";
    new_command += realpath(options.validator_script, NULL);
    new_command += " -i ";
    new_command += stripped_name;
    new_command += " 2> /dev/null";

    for (int i = 0; i < PRUNE_ITERS; i++) {
        auto temp = program;
        auto temp_f = new std::ofstream(stripped_name);
        std::vector<const IR::Statement *> to_prune =
            collect_statements(temp, max_statements);
        // Removes all the nodes it recieves from the vector
        P4PRUNER::Pruner *pruner = new P4PRUNER::Pruner(to_prune);
        temp = temp->apply(*pruner);

        P4::ToP4 *temp_p4 = new P4::ToP4(temp_f, false);
        temp->apply(*temp_p4);

        int exit_code = system(new_command.c_str());

        // If we dont see any changes for 7 iterations we probabbly are done
        if (temp == program) {
            same_before_pruning++;
        }
        if (same_before_pruning >= 7) {
            break;
        }
        // if got the right exit code, then modify the original program, if not
        // then choose a smaller bank of statements to remove now.
        INFO("Going from max statements: " << max_statements);
        if (exit_code != required_exit_code) {
            if (max_statements > 1) {
                max_statements /= 2;
            }
            INFO(" to max statements: "
                 << max_statements
                 << "\n```````````Failure````````````````````````\n");

        } else {
            program = temp;
            max_statements += 2;
            INFO(" to max statements: "
                 << max_statements
                 << "\n```````````Success````````````````````````\n");
        }
    }
    // Done pruning
    // program = temp;

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

    INFO("\nChecking " << options.file);
    // Assemble the validator command
    cstring command = "python3 ";
    command += realpath(options.validator_script, NULL);
    command += " -i ";
    command += realpath(options.file, NULL);
    command += " 2> /dev/null";

    // Retrieve the exit code from the unchanged program
    int required_exit_code = system(command.c_str());
    INFO("Got code : " << required_exit_code << " for the main file");
    program = P4::parseP4File(options);

    if (program != nullptr && ::errorCount() == 0) {
        program = prune_statements(program, options, required_exit_code);
        if (options.print_pruned) {
            P4::ToP4 *after = new P4::ToP4(&std::cout, false);
            program->apply(*after);
        }
        // if the emit flag is enabled, also emit the new p4 version
        if (options.emit_p4) {
            auto stripped_name = remove_extension(options.file);
            auto p4_ostream = openFile(stripped_name + "_stripped.p4", false);
            P4::ToP4 *top4 = new P4::ToP4(p4_ostream, false);
            program->apply(*top4);
        }
    }

    return ::errorCount() > 0;
}
