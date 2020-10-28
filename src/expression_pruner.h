
#ifndef _EXPRESSION_PRUNER_H
#define _EXPRESSION_PRUNER_H
#include <vector>

#include "ir/ir.h"
#include "pruner_options.h"

namespace P4PRUNER {

class ExpressionPruner : public Transform {
 public:
    ExpressionPruner() { setName("Pruner"); }

    const IR::Node *preorder(const IR::Neg *expr);
    const IR::Node *preorder(const IR::Cmpl *expr);
    const IR::Node *preorder(const IR::Mul *expr);
    const IR::Node *preorder(const IR::Div *expr);
    const IR::Node *preorder(const IR::Add *expr);
    const IR::Node *preorder(const IR::AddSat *expr);
    const IR::Node *preorder(const IR::Sub *expr);
    const IR::Node *preorder(const IR::SubSat *expr);
    const IR::Node *preorder(const IR::BAnd *expr);
    const IR::Node *preorder(const IR::BOr *expr);
    const IR::Node *preorder(const IR::BXor *expr);

    /* these are shifts, we should only use the left-hand value */
    const IR::Node *preorder(const IR::Mod *expr);
    const IR::Node *preorder(const IR::Shl *expr);
    const IR::Node *preorder(const IR::Shr *expr);

    // To be Implemented -----------

    /* these need to result in a boolean if we prune them */
    // const IR::Node *preorder(const IR::LAnd *expr);%
    // const IR::Node *preorder(const IR::Neq *expr);
    // const IR::Node *preorder(const IR::Lss *expr);
    // const IR::Node *preorder(const IR::Leq *expr);
    // const IR::Node *preorder(const IR::Grt *expr);
    // const IR::Node *preorder(const IR::Geq *expr);

    // const IR::Node *preorder(const IR::Mask *m);
    // const IR::Node *preorder(const IR::Range *r);
    // const IR::Node *preorder(const IR::Cast *c);
    // const IR::Node *preorder(const IR::Concat *c);
    // const IR::Node *preorder(const IR::Slice *s);
    // const IR::Node *preorder(const IR::Mux *m);
    // const IR::Node *preorder(const IR::Member *m);
    // const IR::Node *preorder(const IR::PathExpression *p);
    // const IR::Node *preorder(const IR::SerEnumMember *m);
    // const IR::Node *preorder(const IR::DefaultExpression *de);
    // const IR::Node *preorder(const IR::ListExpression *le);
    // const IR::Node *preorder(const IR::TypeNameExpression *tn);
    // const IR::Node *preorder(const IR::NamedExpression *ne);
    // const IR::Node *preorder(const IR::StructExpression *sie);
    // const IR::Node *preorder(const IR::ConstructorCallExpression *cc);
    // const IR::Node *preorder(const IR::MethodCallExpression *mce);

    const IR::Node *preorder(const IR::StructExpression *s);
};

const IR::P4Program *prune_expressions(const IR::P4Program *program,
                                       P4PRUNER::PrunerOptions options,
                                       int required_exit_code);

const IR::Node *pick_side_binary(const IR::Operation_Binary *s);

}  // namespace P4PRUNER

#endif /* _EXPRESSION_PRUNER_H */
