#ifndef _PRUNER_UTIL_H_
#define _PRUNER_UTIL_H_

#include "ir/ir.h"

#include "pruner_options.h"

#define INFO(x) std::cout << x << std::endl;

// define some fixed constants
#define PRUNE_STMT_MAX 100
#define PRUNE_ITERS 50
#define NO_CHNG_ITERS 7
cstring STRIPPED_NAME;

namespace P4PRUNER {

struct PrunerConfig {
    int exit_code;
    cstring validation_bin;
    cstring prog_before;
    cstring prog_post;
    cstring compiler;
    cstring output_dir;
    PrunerConfig()
        : exit_code(0), validation_bin(nullptr), prog_before{nullptr},
          prog_post(nullptr), compiler(nullptr), output_dir(nullptr) {}
};

void set_seed(int64_t seed);
int64_t get_rnd_int(int64_t min, int64_t max);
big_int get_rnd_big_int(big_int min, big_int max);
double get_rnd_pct();

int get_exit_code(cstring name, cstring validator_bin);
cstring remove_extension(cstring filename);
void emit_p4_program(const IR::P4Program *program, cstring prog_name);
void print_p4_program(const IR::P4Program *program);
void set_stripped_program_name(cstring program_name);

bool compare_files(const IR::P4Program *prog_before,
                   const IR::P4Program *prog_after);

double measure_pct(const IR::P4Program *prog_before,
                   const IR::P4Program *prog_after);
int check_pruned_program(const IR::P4Program **orig_program,
                         const IR::P4Program *pruned_program,
                         P4PRUNER::PrunerConfig pruner_conf);
} // namespace P4PRUNER

#endif /* _PRUNER_UTIL_H_ */
