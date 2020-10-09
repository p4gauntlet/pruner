#ifndef _P4PRUNER_H
#define _P4PRUNER_H

#include "ir/ir.h"

namespace P4PRUNER {

#define INFO(x) std::cout << x << std::endl;

class Pruner : public Transform {
  public:
    std::vector<IR::Node *> to_prune;
    Pruner(std::vector<IR::Node *> _to_prune) {
        setName("Pruner");
        to_prune = _to_prune;
    }
    IR::Node *preorder(IR::Statement *s);
    IR::Node *preorder(IR::BlockStatement *s);
};

class Collector : public Inspector {
  public:
    Collector() { setName("Collector"); }

    bool preorder(IR::Statement *s);
    bool preorder(IR::BlockStatement *s);
    std::vector<IR::Node *> to_prune;
};

} // namespace P4PRUNER

#endif /* _P4PRUNER_H */
