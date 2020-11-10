#ifndef _PRUNER_UTIL_H_
#define _PRUNER_UTIL_H_

#include "ir/ir.h"

#include "pruner_options.h"

#define INFO(x) std::cout << x << std::endl;

// define some fixed constants
#define PRUNE_STMT_MAX 100
#define PRUNE_ITERS 50
#define NO_CHNG_ITERS 7

namespace P4PRUNER {

struct PrunerConfig {
    int exit_code;
    cstring validation_bin;
    cstring prog_before;
    cstring prog_post;
    cstring compiler;
    cstring working_dir;
    cstring out_file_name;
    PrunerConfig()
        : exit_code(0), validation_bin(nullptr), prog_before{nullptr},
          prog_post(nullptr), compiler(nullptr), working_dir(nullptr),
          out_file_name(nullptr) {}
};

void set_seed(int64_t seed);
int64_t get_rnd_int(int64_t min, int64_t max);
big_int get_rnd_big_int(big_int min, big_int max);
double get_rnd_pct();

bool file_exists(cstring file_path);
void remove_file(cstring file_path);
cstring remove_extension(cstring file_path);
cstring get_file_stem(cstring file_path);

int get_exit_code(cstring name, P4PRUNER::PrunerConfig pruner_conf);
void emit_p4_program(const IR::P4Program *program, cstring prog_name);
void print_p4_program(const IR::P4Program *program);

bool compare_files(const IR::P4Program *prog_before,
                   const IR::P4Program *prog_after);

double measure_pct(const IR::P4Program *prog_before,
                   const IR::P4Program *prog_after);
int check_pruned_program(const IR::P4Program **orig_program,
                         const IR::P4Program *pruned_program,
                         P4PRUNER::PrunerConfig pruner_conf);
} // namespace P4PRUNER

#endif /* _PRUNER_UTIL_H_ */
