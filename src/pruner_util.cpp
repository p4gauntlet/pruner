#include <fstream>

#include "frontends/p4/toP4/toP4.h"

#include "pruner_util.h"

namespace P4PRUNER {

int get_exit_code(cstring name, P4PRUNER::PrunerOptions options) {
    cstring command = "python3 ";
    command += realpath(options.validator_script, NULL);
    command += " -i ";
    command += name;
    command += " 2> /dev/null";
    return system(command.c_str());
}

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

void emit_p4_program(const IR::P4Program *program, cstring prog_name) {
    auto temp_f = new std::ofstream(prog_name);
    P4::ToP4 *temp_p4 = new P4::ToP4(temp_f, false);
    program->apply(*temp_p4);
}

void print_p4_program(const IR::P4Program *program) {
    P4::ToP4 *print_p4 = new P4::ToP4(&std::cout, false);
    program->apply(*print_p4);
}

void set_stripped_program_name(cstring program_name) {
    STRIPPED_NAME = remove_extension(program_name);
    STRIPPED_NAME += "_stripped.p4";
}

} // namespace P4PRUNER
