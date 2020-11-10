#include "prune_unused.h"
#include "frontends/p4/sideEffects.h"
#include "ir/visitor.h"
#include "pruner_util.h"
namespace P4PRUNER {

const IR::Node *PruneUnused::preorder(IR::Declaration_Variable *decl) {
    prune();
    if (decl->initializer == nullptr)
        return process(decl);
    if (!P4::SideEffects::check(decl->initializer, nullptr, nullptr))
        return process(decl);
    return decl;
}

const IR::Node *PruneUnused::preorder(IR::Declaration_Instance *decl) {
    // Don't delete instances; they may have consequences on the control-plane
    // API
    // if (decl->getName().name == IR::P4Program::main &&
    //     getParent<IR::P4Program>())
    //     return decl;

    const IR::Node *preorder(IR::Type_Error * type) {
        // prune();
        return process(type);
    }
    const IR::Node *preorder(IR::Type_StructLike * type) {
        // prune();
        return process(type);
    }
    const IR::Node *preorder(IR::Type_Extern * type) {
        // prune();
        return process(type);
    }
    const IR::Node *preorder(IR::Type_Method * type) {
        // prune();
        return process(type);
    }

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

} // namespace P4PRUNER
