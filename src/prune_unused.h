#ifndef _PRUNE_UNUSED_H_
#define _PRUNE_UNUSED_H_

#include "frontends/common/resolveReferences/resolveReferences.h"
#include "frontends/p4/unusedDeclarations.h"
#include "ir/ir.h"

namespace P4PRUNER {

class PruneUnused : public P4::RemoveUnusedDeclarations {

    const IR::Node *process(const IR::IDeclaration *decl);

 public:
    explicit PruneUnused(const P4::ReferenceMap *_refMap) {
        refMap = _refMap;
        // setName("PruneUnused");
    }

    Visitor::profile_t init_apply(const IR::Node *root) override;

    const IR::Node *preorder(IR::P4Control *cont) override;
    const IR::Node *preorder(IR::P4Parser *cont) override;
    const IR::Node *preorder(IR::P4Table *cont) override;
    const IR::Node *preorder(IR::ParserState *state) override;
    // const IR::Node *preorder(IR::Type_Enum *type) override;
    // const IR::Node *preorder(IR::Type_SerEnum *type) override;

    const IR::Node *preorder(IR::Declaration_Instance *decl) override;

    const IR::Node *preorder(IR::Type_Error *type) override;
    // FIXME
    // makeshift solution for right now /////////////////////////////////
    // const IR::Node *preorder(IR::Type_StructLike *type);
    // const IR::Node *preorder(IR::Type_Extern *type);
    // const IR::Node *preorder(IR::Declaration_MatchKind *decl);
    // const IR::Node *preorder(IR::Type_Method *type);
    ///////////////////////////////////////////////////////////////////////
    const IR::Node *preorder(IR::Parameter *param) override { return param; }
    const IR::Node *preorder(IR::NamedExpression *ne) override { return ne; }
    const IR::Node *preorder(IR::TypeParameters *p) override {
        prune();
        return p;
    }
    const IR::Node *preorder(IR::Declaration_Variable *decl) override;
    const IR::Node *preorder(IR::Declaration *decl) override {
        return process(decl);
    }
    const IR::Node *preorder(IR::Type_Declaration *decl) override {
        return process(decl);
    }
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
