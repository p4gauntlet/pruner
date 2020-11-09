#include "prune_unused.h"
#include "frontends/p4/sideEffects.h"
#include "ir/visitor.h"
namespace P4PRUNER {

Visitor::profile_t PruneUnused::init_apply(const IR::Node *node) {
    INFO("Reference map " << refMap);
    return Transform::init_apply(node);
}

const IR::Node *PruneUnused::preorder(IR::Type_Error *type) {
    prune();
    if (!refMap->isUsed(getOriginal<IR::Type_Error>())) {
        INFO("Removing " << type);
        return nullptr;
    }
    return type;
}
// FIXME
/* This doesnt seem to work right now
const IR::Node *PruneUnused::preorder(IR::Declaration_MatchKind *decl) {

    prune();
    if (!refMap->isUsed(getOriginal<IR::Declaration_MatchKind>())) {
        INFO("Removing " << type);
        return nullptr;
    }
    return type;
}
const IR::Node *PruneUnused::preorder(IR::Type_StructLike *type) {

    prune();
    if (!refMap->isUsed(getOriginal<IR::Type_StructLike>())) {
        INFO("Removing " << type);
        return nullptr;
    }
    return type;
}
const IR::Node *PruneUnused::preorder(IR::Type_Extern *type) {
    prune();
    if (!refMap->isUsed(getOriginal<IR::Type_Extern>())) {
        INFO("Removing " << type);
        return nullptr;
    }
    return type;
}
const IR::Node *PruneUnused::preorder(IR::Type_Method *type) {

    prune();
    if (!refMap->isUsed(getOriginal<IR::Type_Method>())) {
        INFO("Removing " << type);
        return nullptr;
    }
    return type;
}

const IR::Node *PruneUnused::preorder(IR::Type_Enum *type) {
    prune(); // never remove individual enum members
    if (!refMap->isUsed(getOriginal<IR::Type_Enum>())) {
        INFO("Removing " << type);
        return nullptr;
    }
    return type;
}

const IR::Node *PruneUnused::preorder(IR::Type_SerEnum *type) {
    prune(); // never remove individual enum members
    if (!refMap->isUsed(getOriginal<IR::Type_SerEnum>())) {
        INFO("Removing " << type);
        return nullptr;
    }
    return type;
}
*/

const IR::Node *PruneUnused::preorder(IR::P4Control *cont) {
    if (!refMap->isUsed(getOriginal<IR::IDeclaration>())) {
        INFO("Removing " << cont);
        prune();
        return nullptr;
    }

    visit(cont->controlLocals, "controlLocals");
    visit(cont->body);
    prune();
    return cont;
}

const IR::Node *PruneUnused::preorder(IR::P4Parser *cont) {
    if (!refMap->isUsed(getOriginal<IR::IDeclaration>())) {
        INFO("Removing " << cont);
        prune();
        return nullptr;
    }

    visit(cont->parserLocals, "parserLocals");
    visit(cont->states, "states");
    prune();
    return cont;
}

const IR::Node *PruneUnused::preorder(IR::P4Table *table) {
    if (!refMap->isUsed(getOriginal<IR::IDeclaration>())) {
        INFO("Removing " << table);
        table = nullptr;
    }
    prune();
    return table;
}

const IR::Node *PruneUnused::preorder(IR::Declaration_Variable *decl) {
    prune();
    if (decl->initializer == nullptr)
        return process(decl);
    if (!P4::SideEffects::check(decl->initializer, nullptr, nullptr))
        return process(decl);
    return decl;
}

const IR::Node *PruneUnused::process(const IR::IDeclaration *decl) {
    INFO("Visiting " << decl);
    if (decl->getName().name == IR::ParserState::verify &&
        getParent<IR::P4Program>())
        return decl->getNode();
    if (refMap->isUsed(getOriginal<IR::IDeclaration>()))
        return decl->getNode();
    INFO("Removing " << getOriginal());
    prune(); // no need to go deeper
    return nullptr;
}

const IR::Node *PruneUnused::preorder(IR::Declaration_Instance *decl) {
    // Don't delete instances; they may have consequences on the control-plane
    // API
    // if (decl->getName().name == IR::P4Program::main &&
    //     getParent<IR::P4Program>())
    //     return decl;
    if (!refMap->isUsed(getOriginal<IR::Declaration_Instance>())) {

        // We won't delete extern instances; these may be useful even if not
        // references.

        ///////
        // Try deleting everything regardless
        ///////

        // auto type = decl->type;
        // if (type->is<IR::Type_Specialized>())
        //     type = type->to<IR::Type_Specialized>()->baseType;
        // if (type->is<IR::Type_Name>())
        //     type = refMap->getDeclaration(type->to<IR::Type_Name>()->path,
        //     true)
        //                ->to<IR::Type>();
        // if (!type->is<IR::Type_Extern>())
        //     return process(decl);
        // prune();
        return process(decl);
    }
    // lets try deleting these too // don't scan the initializer: we don't want
    // to delete virtual methods

    return process(decl);
}

const IR::Node *PruneUnused::preorder(IR::ParserState *state) {
    if (state->name == IR::ParserState::accept ||
        state->name == IR::ParserState::reject ||
        state->name == IR::ParserState::start)
        return state;

    if (refMap->isUsed(getOriginal<IR::ParserState>()))
        return state;
    INFO("Removing " << state);
    prune();
    return nullptr;
}

} // namespace P4PRUNER
