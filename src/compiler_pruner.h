#ifndef _COMPILER_PRUNER_H
#define _COMPILER_PRUNER_H

#include "ir/ir.h"
#include "pruner_options.h"

namespace P4PRUNER {

const IR::P4Program *apply_compiler_passes(const IR::P4Program *program,
                                           P4PRUNER::PrunerOptions options,
                                           int required_exit_code);

} // namespace P4PRUNER

#endif /* _COMPILER_PRUNER_H */
