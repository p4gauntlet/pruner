#include "pruner.h"

namespace P4PRUNER {

IR::Node *Pruner::preorder(IR::Statement *s) {
    return rand() % 100 < 10 ? nullptr : s;
}

IR::Node *Pruner::preorder(IR::BlockStatement *s) {
    for (auto c : s->components) {
        visit(c);
    }

    return s;
}
} // namespace P4PRUNER
