#include <fstream>

#include "frontends/common/parseInput.h"
#include "frontends/p4/toP4/toP4.h"
#include "ir/ir.h"
#include "lib/cstring.h"
#include "lib/nullstream.h"

#include "unistd.h"

#include "pruner.h"
#include "pruneroptions.h"

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

    if (options.file == nullptr) {
        options.usage();
        return 1;
    }

    const IR::P4Program *program = nullptr;
    // std::cout << "\nChecking " << options.file;
    cstring command = "python3 /home/roborobo/projects/gauntlet_paper/gauntlet/"
                      "validate_p4_translation.py -i ";
    command += realpath(options.file, NULL);
    // command += " > /dev/null";
    // command += options.file;
    // std::wcout << command;
    int required_exit_code = system(command.c_str());
    printf("%s\n", command);
    std::cout << "Got code :" << required_exit_code << " for the main file";
    program = P4::parseP4File(options);

    if (program != nullptr && ::errorCount() == 0) {
        // P4::ToP4 *before = new P4::ToP4(&std::cout, false);
        // program->apply(*before);

        for (int j = 0; j < 10; j++) {
            P4PRUNER::Pruner *pruner = new P4PRUNER::Pruner();
            for (int i = 0; i < 100; i++) {
                auto temp = program;
                temp = temp->apply(*pruner);
                auto temp_f = new std::ofstream("temp.p4");

                P4::ToP4 *temp_p4 = new P4::ToP4(temp_f, false);
                temp->apply(*temp_p4);
                cstring new_command = "python3 "
                                      "/home/roborobo/projects/gauntlet_paper/"
                                      "gauntlet/validate_p4_translation.py -i ";
                new_command += realpath("./temp.p4", NULL);
                new_command += " 2> /dev/null";
                // printf("For the changed file : %s\n", new_command);
                int exit_code = system(new_command.c_str());

                if (exit_code == required_exit_code) {
                    program = temp;
                    std::cout << "\n\n\nSuccess\n\n\n";
                    break;
                } else {
                    std::cout << "\n \nGot diff error code " << exit_code
                              << "instead of " << required_exit_code
                              << "\n\n\n";
                }
            }
        }

        std::cout << "\n\n\n**********new*********\n\n\n";
        P4::ToP4 *after = new P4::ToP4(&std::cout, false);
        program->apply(*after);

        // if the emit flag is enabled, also emit the new p4 version
        if (options.emit_p4) {
            auto stripped_name = remove_extension(options.file);
            printf("%s\n", stripped_name);
            auto p4_ostream = openFile(stripped_name + "_stripped.p4", false);
            P4::ToP4 *top4 = new P4::ToP4(p4_ostream, false);
            program->apply(*top4);
        }
    }

    return ::errorCount() > 0;
}
