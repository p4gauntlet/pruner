#include "expression_pruner.h"
#include "ir/visitor.h"
#include "pruner_util.h"

namespace P4PRUNER {

IR::Node *ExpressionPruner::preorder(IR::Operation_Binary *s) {

    IR::Node *to_remove =
        rand() < 0.5 ? (IR::Node *)s->left : (IR::Node *)s->right;
    visit(to_remove);
}

IR::Node *ExpressionPruner::preorder(IR::Operation_Unary *s) {
    return rand() < 0.5 ? (IR::Node *)s->expr : (IR::Node *)s;
}

IR::Node *ExpressionPruner::preorder(IR::MethodCallExpression *s) {
    return (IR::Node *)s;
}

IR::Node *ExpressionPruner::preorder(IR::StructExpression *s) {

    for (auto c : s->components) {
        visit(c);
    }

    return (IR::Node *)s;
}
const IR::P4Program *remove_expressions(const IR::P4Program *temp) {
    // Removes all the nodes it recieves from the vector
    P4PRUNER::ExpressionPruner *expression_pruner =
        new P4PRUNER::ExpressionPruner();
    temp = temp->apply(*expression_pruner);
    return temp;
}

const IR::P4Program *prune_expressions(const IR::P4Program *program,
                                       P4PRUNER::PrunerOptions options,
                                       int required_exit_code) {
    int same_before_pruning = 0;
    uint64_t max_statements = PRUNE_STMT_MAX;
    INFO("\nPruning expressions now \n")
    for (int i = 0; i < PRUNE_ITERS; i++) {
        INFO("Trying with  " << max_statements << " statements");
        auto temp = program;
        temp = remove_expressions(temp);
        emit_p4_program(temp, STRIPPED_NAME);
        int exit_code = get_exit_code(STRIPPED_NAME, options);

        // If we don't see any changes for NO_CHNG_ITERS iterations we probably
        // are done
        if (temp == program) {
            same_before_pruning++;
            if (same_before_pruning >= NO_CHNG_ITERS) {
                break;
            }
        }
        // if got the right exit code, then modify the original program, if not
        // then choose a smaller bank of statements to remove now.
        if (exit_code != required_exit_code) {
            INFO("FAILED");
            if (max_statements > 1) {
                max_statements /= 2;
            }

        } else {
            INFO("PASSED");
            program = temp;
            max_statements += 2;
        }
    }
    // Done pruning
    return program;
}

} // namespace P4PRUNER
