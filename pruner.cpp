#include "pruner.h"

namespace P4PRUNER {

IR::Node *Pruner::preorder(IR::Statement *s) {

    // return rand() % 100 < 10 ? nullptr : s;
    for (int i = 0; i < to_prune.size(); i++) {

        // This seems to be working
        // if (to_prune.at(i)->getNode()->equiv(*s->getNode())) {

        // This seems not to
        if (to_prune.at(i) == s)
            return nullptr;
    }
    return s;
}
IR::Node *Pruner::preorder(IR::BlockStatement *s) {
    for (auto c : s->components) {
        visit(c);
    }

    return (IR::Node *)s;
}
Visitor::profile_t Collector::init_apply(const IR::Node *node) {
    return Inspector::init_apply(node);
}

bool Collector::preorder(const IR::Statement *s) {
    // if (to_prune.size() <= 25 && rand() % 100 < 10 )
    if (to_prune.size() <= 25) {
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

} // namespace P4PRUNER
