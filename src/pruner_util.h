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

int get_exit_code(cstring name, P4PRUNER::PrunerOptions options);
cstring remove_extension(cstring filename);
void emit_p4_program(const IR::P4Program *program, cstring prog_name);
void print_p4_program(const IR::P4Program *program);
void set_stripped_program_name(cstring program_name);


} // namespace P4PRUNER

#endif /* _PRUNER_UTIL_H_ */
