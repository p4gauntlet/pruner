#ifndef _PRUNE_UNUSED_H_
#define _PRUNE_UNUSED_H_

#include "frontends/common/resolveReferences/resolveReferences.h"
#include "frontends/p4/unusedDeclarations.h"
#include "ir/ir.h"

namespace P4PRUNER {

class PruneUnused : public P4::RemoveUnusedDeclarations {
    const P4::ReferenceMap *refMap;

    // bool giveWarning(const IR::Node *node);
    const IR::Node *process(const IR::IDeclaration *decl);

 public:
    explicit PruneUnused(const P4::ReferenceMap *refMap)
        : P4::RemoveUnusedDeclarations(refMap) {
        CHECK_NULL(refMap);
        setName("PruneUnused");
    }

    const IR::Node *preorder(IR::Type_Error *type) override;
    const IR::Node *preorder(IR::Type_StructLike *type) override;
    const IR::Node *preorder(IR::Type_Extern *type) override;
    const IR::Node *preorder(IR::Type_Method *type) override;
    const IR::Node *preorder(IR::Declaration_Variable *decl) override;
    const IR::Node *preorder(IR::Declaration_Instance *decl) override;
};

class PruneAllUnused : public PassManager {
 public:
    explicit PruneAllUnused(P4::ReferenceMap *refMap) {
        passes.emplace_back(new PassRepeated{new P4::ResolveReferences(refMap),
                                             new PruneUnused(refMap)});
    }
};

} // namespace P4PRUNER

#endif /* _PRUNE_UNUSED_H_ */
