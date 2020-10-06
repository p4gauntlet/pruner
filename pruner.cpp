#include "pruner.h"

namespace P4PRUNER {

IR::Node *Pruner::preorder(IR::Statement *s) {

    // bool found = false;
    for (int i = 0; i < checked.size(); i++) {
        if (s == checked.at(i)) {
            // found = true;
            return s;
        }
    }

    checked.push_back(s);

    return nullptr;
}
} // namespace P4PRUNER
