#ifndef _P4PRUNER_H
#define _P4PRUNER_H

#include "ir/ir.h"

namespace P4PRUNER {

#define INFO(x) std::cout << x << std::endl;

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
    Collector(int _max_statements) {
        setName("Collector");
        max_statements = _max_statements;
    }
    Visitor::profile_t init_apply(const IR::Node *node) override;
    bool preorder(const IR::Statement *s) override;
    bool preorder(const IR::BlockStatement *s) override;
    std::vector<const IR::Statement *> to_prune;
    int max_statements;
};

} // namespace P4PRUNER

#endif /* _P4PRUNER_H */
