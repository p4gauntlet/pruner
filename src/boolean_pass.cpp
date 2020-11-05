#include "boolean_pass.h"
#include "ir/visitor.h"
#include "pruner_util.h"

namespace P4PRUNER {

const IR::Node *rand_bool_literal() {
    auto decision = get_rnd_pct();

    return new IR::BoolLiteral(decision < 0.5);
}

const IR::Node *BoolExpressionPruner::postorder(IR::LAnd *) {
    return rand_bool_literal();
}
const IR::Node *BoolExpressionPruner::postorder(IR::Neq *) {
    return rand_bool_literal();
}
const IR::Node *BoolExpressionPruner::postorder(IR::Lss *) {
    return rand_bool_literal();
}
const IR::Node *BoolExpressionPruner::postorder(IR::Leq *) {
    return rand_bool_literal();
}
const IR::Node *BoolExpressionPruner::postorder(IR::Grt *) {
    return rand_bool_literal();
}
const IR::Node *BoolExpressionPruner::postorder(IR::Geq *) {
    return rand_bool_literal();
}

const IR::Node *BoolExpressionPruner::postorder(IR::LOr *) {
    return rand_bool_literal();
}

const IR::Node *BoolExpressionPruner::postorder(IR::Equ *) {
    return rand_bool_literal();
}

const IR::P4Program *remove_bool_expressions(const IR::P4Program *temp) {
    // Removes all the nodes it recieves from the vector
    P4PRUNER::BoolExpressionPruner *bool_expression_pruner =
        new P4PRUNER::BoolExpressionPruner();
    temp = temp->apply(*bool_expression_pruner);
    return temp;
}

const IR::P4Program *prune_bool_expressions(const IR::P4Program *program,
                                            P4PRUNER::PrunerOptions options,
                                            int required_exit_code) {
    int same_before_pruning = 0;
    INFO("\nPruning boolean expressions now \n")
    for (int i = 0; i < PRUNE_ITERS; i++) {
        auto temp = program;
        temp = remove_bool_expressions(temp);
        emit_p4_program(temp, STRIPPED_NAME);
        if (compare_files(temp, program)) {
            INFO("Skipping due to no change");
            same_before_pruning++;
            if (same_before_pruning >= NO_CHNG_ITERS) {
                break;
            }
            continue;
        }
        int exit_code = get_exit_code(STRIPPED_NAME, options.validator_script);

        // if got the right exit code, then modify the original program, if not
        // then choose a smaller bank of statements to remove now.
        if (exit_code != required_exit_code) {
            INFO("FAILED");
        } else {
            INFO("PASSED: Reduced by " << measure_pct(program, temp) << " %");
            program = temp;
        }
    }
    // Done pruning
    return program;
} // namespace P4PRUNER

} // namespace P4PRUNER
