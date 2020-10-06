#include "pruner.h"

namespace P4PRUNER {

IR::Node *Pruner::preorder(IR::Statement *s) {

    if (s->is<IR::BlockStatement>()) {
        // its a bit hard to prune block statements for now
        return s;
    }

    // bool found = false;
    for (int i = 0; i < checked.size(); i++) {
        if (s->getNode()->equiv(*checked.at(i))) {
            // found = true ;
            // printf("Ofcourse thiss is working\n");
            end_apply();
            return s;
        }
    }
    checked.push_back(s->getNode());

    return nullptr;
}
} // namespace P4PRUNER
