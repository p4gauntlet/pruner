
#ifndef _SIMPLIFIER_H
#define _SIMPLIFIER_H
#include <vector>

#include "ir/ir.h"
#include "pruner_options.h"

namespace P4PRUNER {

class Simplifier : public Transform {
  public:
    Simplifier() { setName("Pruner"); }
    IR::Node *preorder(IR::Operation_Binary *s);
};

const IR::P4Program *simplify_expressions(const IR::P4Program *program,
                                          P4PRUNER::PrunerOptions options,
                                          int required_exit_code);

} // namespace P4PRUNER

#endif /* _SIMPLIFIER_H */
