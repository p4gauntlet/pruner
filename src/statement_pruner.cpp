#include "statement_pruner.h"
#include "ir/visitor.h"
#include "pruner_util.h"

namespace P4PRUNER {

const IR::Node *Pruner::preorder(IR::Statement *s) {
    for (uint64_t i = 0; i < to_prune.size(); i++) {
        if (*to_prune.at(i) == *s) {
            return nullptr;
        }
    }
    return s;
}

const IR::Node *Pruner::preorder(IR::BlockStatement *s) {
    for (auto c : s->components) {
        visit(c);
    }

    return s;
}

const IR::Node *Pruner::preorder(IR::ReturnStatement *s) {
    // do not prune return statements
    return s;
}

Visitor::profile_t Collector::init_apply(const IR::Node *node) {
    return Inspector::init_apply(node);
}

bool Collector::preorder(const IR::Statement *s) {
    if (to_prune.size() <= max_statements && (get_rnd_pct() < 0.5)) {
        to_prune.push_back(s);
    }

    return true;
}

bool Collector::preorder(const IR::BlockStatement *s) {
    for (auto c : s->components) {
        visit(c);
    }

    return true;
}

const std::vector<const IR::Statement *>
collect_statements(const IR::P4Program *temp, int max) {
    // An inspector that collects some statements at random
    P4PRUNER::Collector *collector = new P4PRUNER::Collector(max);
    temp->apply(*collector);
    return collector->to_prune;
}

const IR::P4Program *
remove_statements(const IR::P4Program *temp,
                  std::vector<const IR::Statement *> to_prune) {
    // Removes all the nodes it recieves from the vector
    P4PRUNER::Pruner *pruner = new P4PRUNER::Pruner(to_prune);
    temp = temp->apply(*pruner);
    return temp;
}

const IR::P4Program *prune_statements(const IR::P4Program *program,
                                      P4PRUNER::PrunerOptions options,
                                      int required_exit_code) {
    int same_before_pruning = 0;
    uint64_t max_statements = PRUNE_STMT_MAX;

    for (int i = 0; i < PRUNE_ITERS; i++) {
        INFO("Trying with  " << max_statements << " statements");
        auto temp = program;
        std::vector<const IR::Statement *> to_prune =
            collect_statements(temp, max_statements);
        temp = remove_statements(temp, to_prune);
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
            if (max_statements > 1) {
                max_statements /= 2;
            }

        } else {
            INFO("PASSED: Reduced by " << measure_pct(program, temp) << " %");

            program = temp;
            max_statements += 2;
        }
    }
    // Done pruning
    return program;
} // namespace P4PRUNER

} // namespace P4PRUNER
