
#ifndef _BOOLEAN_PASS_H
#define _BOOLEAN_PASS_H
#include <vector>

#include "ir/ir.h"
#include "pruner_options.h"

namespace P4PRUNER {

class BoolExpressionPruner : public Transform {
 public:
    BoolExpressionPruner() { visitDagOnce = true; }

    const IR::Node *postorder(IR::LAnd *expr);
    const IR::Node *postorder(IR::Neq *expr);
    const IR::Node *postorder(IR::Lss *expr);
    const IR::Node *postorder(IR::Leq *expr);
    const IR::Node *postorder(IR::Grt *expr);
    const IR::Node *postorder(IR::Geq *expr);
};

const IR::P4Program *prune_bool_expressions(const IR::P4Program *program,
                                            P4PRUNER::PrunerOptions options,
                                            int required_exit_code);

} // namespace P4PRUNER

#endif /* _BOOLEAN_PASS_H */
