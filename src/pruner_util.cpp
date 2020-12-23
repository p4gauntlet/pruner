#include <sys/stat.h>

#include <fstream>
#include <memory>
#include <string>

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

bool file_exists(cstring file_path) {
    struct stat buffer;
    INFO("Checking if " << file_path << " exists.");
    if (stat(file_path, &buffer) != 0) {
        return false;
    }
    return true;
}

void remove_file(cstring file_path) {
    int ret;
    cstring cmd = "rm -rf ";
    cmd += file_path;
    ret = system(cmd);
    if (ret) {
        ::warning("Removing file or folder %s failed.", file_path);
    }
}

cstring get_file_stem(cstring file_path) {
    cstring file_stem;
    cstring stripped_name = P4PRUNER::remove_extension(file_path);
    const char *pos = stripped_name.findlast('/');
    size_t idx = (size_t)(pos - stripped_name);
    if (idx != std::string::npos)
        file_stem = stripped_name.substr(idx + 1);
    else
        file_stem = stripped_name;
    return file_stem;
}

cstring remove_extension(cstring file_path) {
    // find the last dot
    const char *last_dot = file_path.findlast('.');
    // there is no dot in this string, just return the full name
    if (not last_dot) {
        return file_path;
    }
    // otherwise get the index, remove the dot
    size_t idx = (size_t)(last_dot - file_path);
    return file_path.substr(0, idx);
}

ExitInfo get_exit_info(cstring name, P4PRUNER::PrunerConfig pruner_conf) {
    ExitInfo exit_info;
    INFO("Checking exit code.");
    if (pruner_conf.err_type == ErrorType::SemanticBug) {
        cstring command = pruner_conf.validation_bin;
        // suppress output
        command += " -i ";
        command += name;
        // set the output dir
        command += " -o ";
        command += pruner_conf.working_dir;
        command += " -ll CRITICAL ";
        command += " -p ";
        command += pruner_conf.compiler;
        if (pruner_conf.allow_undef) {
            command += " -u ";
        }

        exit_info.exit_code = WEXITSTATUS(system(command.c_str()));
        exit_info.err_msg = cstring("");

    } else {
        exit_info = get_crash_exit_info(name, pruner_conf);
    }
    return exit_info;
}

ExitInfo get_crash_exit_info(cstring name, P4PRUNER::PrunerConfig pruner_conf) {
    // The crash bugs variant of get_exit_code
    ExitInfo exit_info;
    cstring command = pruner_conf.compiler;
    command += " --Wdisable ";
    command += name;
    // Apparently popen doesn't like stderr hence redirecting stderr to stdout
    command += " 2>&1";

    char buffer[1000];
    cstring result = "";
    FILE *pipe = popen(command, "r");
    bool done = false;
    char *saveptr = NULL;
    int newlines = 0;
    try {
        while (fgets(buffer, sizeof buffer, pipe) != NULL && !done) {
            for (int i = 0; i < 1000; i++) {
                if (buffer[i] == '\n') {
                    newlines++;
                    break;
                    if (newlines > 1) {
                        // ignoring the first line
                        strtok_r(buffer, "\n", &saveptr);
                        result += strtok_r(NULL, "\n", &saveptr);

                        done = true;
                        break;
                    }
                }
            }

            result += buffer;
        }
    } catch (...) {
        pclose(pipe);
        throw;
    }
    exit_info.exit_code = WEXITSTATUS(pclose(pipe));
    exit_info.err_msg = result;
    INFO(result);
    return exit_info;
}

ErrorType classify_bug(ExitInfo exit_info) {
    int exit_code = exit_info.exit_code;

    if (exit_code == EXIT_TEST_VALIDATION) {
        return ErrorType::SemanticBug;
    } else if (exit_code == EXIT_TEST_FAILURE) {
        cstring comp = exit_info.err_msg.find("Compiler Bug");

        if (!comp.isNullOrEmpty()) {
            return ErrorType::CrashBug;
        }
        cstring err_msg = exit_info.err_msg.find("error");

        if (!err_msg.isNullOrEmpty()) {
            return ErrorType::Error;
        }
        return ErrorType::Unknown;
    } else if (exit_code == EXIT_TEST_SUCCESS) {
        return ErrorType::Success;
    } else {
        return ErrorType::Unknown;
    }
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

int check_pruned_program(const IR::P4Program **orig_program,
                         const IR::P4Program *pruned_program,
                         P4PRUNER::PrunerConfig pruner_conf) {
    emit_p4_program(pruned_program, pruner_conf.out_file_name);
    if (compare_files(pruned_program, *orig_program)) {
        INFO("File has not changed. Skipping analysis.");
        return EXIT_FAILURE;
    }
    int exit_code =
        get_exit_info(pruner_conf.out_file_name, pruner_conf).exit_code;
    // if got the right exit code, then modify the original program, if not
    // then choose a smaller bank of statements to remove now.
    if (exit_code != pruner_conf.exit_code) {
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
