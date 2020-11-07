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

bool compare_files(const IR::P4Program *prog_before,
                   const IR::P4Program *prog_after) {
    auto before_stream = new std::stringstream;
    auto after_stream = new std::stringstream;

    P4::ToP4 *before = new P4::ToP4(before_stream, false);
    prog_before->apply(*before);

    P4::ToP4 *after = new P4::ToP4(after_stream, false);
    prog_after->apply(*after);

    return before_stream->str() == after_stream->str();
}

double measure_pct(const IR::P4Program *prog_before,
                   const IR::P4Program *prog_after) {
    auto before_stream = new std::stringstream;
    auto after_stream = new std::stringstream;
    P4::ToP4 *before = new P4::ToP4(before_stream, false);
    prog_before->apply(*before);
    auto before_len = before_stream->str().length();

    P4::ToP4 *after = new P4::ToP4(after_stream, false);
    prog_after->apply(*after);
    auto after_len = after_stream->str().length();

    return (before_len - after_len) * (100.0 / before_len);
}

void set_stripped_program_name(cstring program_name) {
    STRIPPED_NAME = remove_extension(program_name);
    STRIPPED_NAME += "_stripped.p4";
}

int check_pruned_program(const IR::P4Program **orig_program,
                         const IR::P4Program *pruned_program,
                         P4PRUNER::PrunerOptions options, int req_exit_code) {
    emit_p4_program(pruned_program, STRIPPED_NAME);
    if (compare_files(pruned_program, *orig_program)) {
        INFO("File has not changed. Skipping analysis.");
        return EXIT_FAILURE;
    }
    int exit_code = get_exit_code(STRIPPED_NAME, options.validator_script);

    // if got the right exit code, then modify the original program, if not
    // then choose a smaller bank of statements to remove now.
    if (exit_code != req_exit_code) {
        INFO("FAILED");
        return EXIT_FAILURE;
    } else {
        INFO("PASSED: Reduced by " << measure_pct(*orig_program, pruned_program)
                                   << " %")
        *orig_program = pruned_program;
        return EXIT_SUCCESS;
    }
}

} // namespace P4PRUNER
