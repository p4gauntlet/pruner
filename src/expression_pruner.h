
#ifndef _EXPRESSION_PRUNER_H
#define _EXPRESSION_PRUNER_H
#include <vector>

#include "ir/ir.h"
#include "pruner_options.h"

namespace P4PRUNER {

class ExpressionPruner : public Transform {
  public:
    ExpressionPruner() { setName("Pruner"); }

    // An example of a binary operation
    const IR::Node *preorder(IR::Add *s);

    // An example of a unary operation
    const IR::Node *preorder(IR::Neg *s);

    const IR::Node *preorder(IR::StructExpression *s);
};

const IR::P4Program *prune_expressions(const IR::P4Program *program,
                                       P4PRUNER::PrunerOptions options,
                                       int required_exit_code);

} // namespace P4PRUNER

#endif /* _EXPRESSION_PRUNER_H */
