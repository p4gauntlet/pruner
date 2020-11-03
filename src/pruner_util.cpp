#include <fstream>
#include <memory>

#include <boost/random.hpp>

#include "frontends/p4/toP4/toP4.h"
#include "pruner_util.h"

namespace P4PRUNER {

static boost::random::mt19937 rng;

void set_seed(int64_t seed) { rng = boost::mt19937(seed); }

int64_t get_rnd_int(int64_t min, int64_t max) {
    boost::random::uniform_int_distribution<int64_t> distribution(min, max);
    return distribution(rng);
}

big_int get_rnd_big_int(big_int min, big_int max) {
    boost::random::uniform_int_distribution<big_int> distribution(min, max);
    return distribution(rng);
}

double get_rnd_pct() {
    boost::random::uniform_real_distribution<double> distribution(0.0, 1.0);
    return distribution(rng);
}

int get_exit_code(cstring name, cstring validator_script) {
    INFO("Checking exit code...");
    cstring command = "python3 ";
    command += realpath(validator_script, NULL);
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

cstring get_checksum(cstring name) {
    std::array<char, 128> buffer;
    cstring result = "";
    cstring command = "sha256sum " + name + " | cut -d \" \" -f1 ";
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), "r"),
                                                  pclose);

    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

bool has_same_checksum(const IR::P4Program *prog_before,
                       const IR::P4Program *prog_after) {
    cstring without_extension = remove_extension(STRIPPED_NAME);
    auto before_file =
        new std::ofstream(without_extension + "_checksum_before.p4");
    auto after_file =
        new std::ofstream(without_extension + "_checksum_after.p4");

    P4::ToP4 *before = new P4::ToP4(before_file, false);
    prog_before->apply(*before);

    P4::ToP4 *after = new P4::ToP4(after_file, false);
    prog_after->apply(*after);

    return !(bool)strcmp(
        get_checksum(without_extension + "_checksum_before.p4"),
        get_checksum(without_extension + "_checksum_after.p4"));
}

double measure_pct(const IR::P4Program *prog_before,
                   const IR::P4Program *prog_after) {
    cstring without_extension = remove_extension(STRIPPED_NAME);
    auto before_file = new std::ofstream(without_extension + "_before.p4");
    auto after_file = new std::ofstream(without_extension + "_after.p4");
    auto before_initial_pos = before_file->tellp();
    P4::ToP4 *before = new P4::ToP4(before_file, false);
    prog_before->apply(*before);
    auto before_len = before_file->tellp() - before_initial_pos;

    auto after_initial_pos = after_file->tellp();
    P4::ToP4 *after = new P4::ToP4(after_file, false);
    prog_after->apply(*after);
    auto after_len = after_file->tellp() - after_initial_pos;

    return (before_len - after_len) * (100.0 / before_len);
}

void set_stripped_program_name(cstring program_name) {
    STRIPPED_NAME = remove_extension(program_name);
    STRIPPED_NAME += "_stripped.p4";
}

} // namespace P4PRUNER
