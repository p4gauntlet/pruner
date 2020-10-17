
#ifndef _STATEMENT_PRUNER_H
#define _STATEMENT_PRUNER_H
#include <vector>

#include "ir/ir.h"
#include "pruner_options.h"

namespace P4PRUNER {

class Pruner : public Transform {
  public:
    std::vector<const IR::Statement *> to_prune;
    Pruner(std::vector<const IR::Statement *> _to_prune) {
        setName("Pruner");
        to_prune = _to_prune;
    }
    IR::Node *preorder(IR::Statement *s);
    IR::Node *preorder(IR::BlockStatement *s);
};

class Collector : public Inspector {
  public:
    Collector(uint64_t _max_statements) {
        setName("Collector");
        max_statements = _max_statements;
    }
    Visitor::profile_t init_apply(const IR::Node *node) override;
    bool preorder(const IR::Statement *s) override;
    bool preorder(const IR::BlockStatement *s) override;
    std::vector<const IR::Statement *> to_prune;
    uint64_t max_statements;
};

const IR::P4Program *prune_statements(const IR::P4Program *program,
                                      P4PRUNER::PrunerOptions options,
                                      int required_exit_code);

} // namespace P4PRUNER

#endif /* _STATEMENT_PRUNER_H */