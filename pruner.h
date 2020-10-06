#ifndef _P4PRUNER_H
#define _P4PRUNER_H

#include "ir/ir.h"

namespace P4PRUNER {

class Pruner : public Transform {
  public:
    // IR::P4Program *program;
    Pruner() {
        setName("Pruner");
        // program = p;
    }

    // IR::Node* preorder(IR::AssignmentStatement *s);
    IR::Node *preorder(IR::Statement *s);
    // void prune_p4();
    std::vector<IR::Node *> checked;
};

} // namespace P4PRUNER

#endif /* _P4PRUNER_H */
