#include "expression_pruner.h"
#include "ir/visitor.h"
#include "pruner_util.h"

namespace P4PRUNER {

const IR::Node *ExpressionPruner::preorder(IR::Add *s) {
    auto decision = (double)rand() / RAND_MAX;
    if (decision < 0.33) {
        // return the left-hand side of the expression
        return s->left;
    } else if (decision < 0.66) {
        // return the right-hand side of the expression
        return s->right;
    }
    // do nothing, just return the node
    return s;
}

const IR::Node *ExpressionPruner::preorder(IR::Neg *s) {
    auto decision = (double)rand() / RAND_MAX;
    if (decision < 0.5) {
        // return the expression without the operation
        return s->expr;
    } else {
        // return the unaltered node
        return s;
    }
}

const IR::Node *ExpressionPruner::preorder(IR::StructExpression *s) {

    for (auto c : s->components) {
        visit(c);
    }

    return s;
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
