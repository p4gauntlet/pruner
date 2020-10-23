#include "simplifier.h"
#include "ir/visitor.h"
#include "pruner_util.h"

namespace P4PRUNER {

IR::Node *Simplifier::preorder(IR::Operation_Binary *s) {
    return rand() < 0.5 ? (IR::Node *)s->left : (IR::Node *)s->right;
}

const IR::P4Program *remove_expressions(const IR::P4Program *temp) {
    // Removes all the nodes it recieves from the vector
    P4PRUNER::Simplifier *simplifier = new P4PRUNER::Simplifier();
    temp = temp->apply(*simplifier);
    return temp;
}

const IR::P4Program *simplify_expressions(const IR::P4Program *program,
                                          P4PRUNER::PrunerOptions options,
                                          int required_exit_code) {
    int same_before_pruning = 0;
    uint64_t max_statements = PRUNE_STMT_MAX;
    INFO("\nSimplifying expressions now \n")
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
