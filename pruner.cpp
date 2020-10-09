#include "pruner.h"

namespace P4PRUNER {

IR::Node *Pruner::preorder(IR::Statement *s) {
    // return rand() % 100 < 10 ? nullptr : s;
    for (int i = 0; i < to_prune.size(); i++) {
        if (to_prune.at(i)->equiv(*s->getNode())) {
            return nullptr;
        }
    }
    return s;
}

IR::Node *Pruner::preorder(IR::BlockStatement *s) {
    for (auto c : s->components) {
        visit(c);
    }

    return (IR::Node *)s;
}

bool Collector::preorder(IR::Statement *s) {
    INFO("What about this now");
    if (to_prune.size() <= 25) {
        to_prune.push_back(s->getNode());
        INFO("DOing this yes i am");
    }

    return true;
}

bool Collector::preorder(IR::BlockStatement *s) {
    for (auto c : s->components) {
        visit(c);
    }

    return true;
}

} // namespace P4PRUNER
