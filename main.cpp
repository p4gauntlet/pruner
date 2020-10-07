#include <fstream>

#include "frontends/common/parseInput.h"
#include "frontends/p4/toP4/toP4.h"
#include "ir/ir.h"
#include "lib/cstring.h"
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

int main(int argc, char *const argv[]) {

    AutoCompileContext autoP4toZ3Context(new P4PRUNER::P4PrunerContext);
    auto &options = P4PRUNER::P4PrunerContext::get().options();
    options.langVersion = CompilerOptions::FrontendVersion::P4_16;

    if (options.process(argc, argv) != nullptr) {
        options.setInputFile();
    }
    if (::errorCount() > 0)
        return 1;

    if (options.file == nullptr || options.validator_script == nullptr) {
        options.usage();
        return 1;
    }

    const IR::P4Program *program = nullptr;
    // std::cout << "\nChecking " << options.file;
    cstring command = "python3 ";
    command += realpath(options.validator_script, NULL);
    command += " -i ";
    command += realpath(options.file, NULL);
    // command += " > /dev/null";
    // command += options.file;
    // std::wcout << command;
    int required_exit_code = system(command.c_str());
    printf("%s\n", command);
    std::cout << "Got code :" << required_exit_code << " for the main file";
    program = P4::parseP4File(options);
    cstring temp_file_name = dirname(realpath(options.file, NULL));
    temp_file_name += "/temp.p4";
    if (program != nullptr && ::errorCount() == 0) {

        for (int j = 0; j < 20; j++) {
            P4PRUNER::Pruner *pruner = new P4PRUNER::Pruner();

            auto temp = program;

            temp = temp->apply(*pruner);

            auto temp_f = new std::ofstream(temp_file_name);

            P4::ToP4 *temp_p4 = new P4::ToP4(temp_f, false);
            temp->apply(*temp_p4);
            cstring new_command = "python3 ";
            // new_command += realpath();
            new_command += realpath(options.validator_script, NULL);
            new_command += " -i ";
            new_command += temp_file_name;
            // printf("For the changed file : %s\n", new_command);
            int exit_code = system(new_command.c_str());

            if (exit_code == required_exit_code) {
                program = temp;
            }
        }

        // std::cout << "\n\n\n**********new*********\n\n\n";
        if (options.print_pruned) {
            P4::ToP4 *after = new P4::ToP4(&std::cout, false);
            program->apply(*after);
        }
        // if the emit flag is enabled, also emit the new p4 version
        if (options.emit_p4) {
            auto stripped_name = remove_extension(options.file);
            // printf("%s\n", stripped_name);
            auto p4_ostream = openFile(stripped_name + "_stripped.p4", false);
            P4::ToP4 *top4 = new P4::ToP4(p4_ostream, false);
            program->apply(*top4);
        }
    }

    return ::errorCount() > 0;
}
