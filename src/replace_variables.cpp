#include "vector"

#include "ir/visitor.h"
#include "replace_variables.h"

#include "frontends/common/constantFolding.h"
#include "frontends/common/resolveReferences/resolveReferences.h"
#include "frontends/p4/createBuiltins.h"
#include "frontends/p4/directCalls.h"
#include "frontends/p4/simplify.h"
#include "frontends/p4/simplifyDefUse.h"
#include "frontends/p4/unusedDeclarations.h"

namespace P4PRUNER {

const IR::Node *ReplaceVariables::postorder(IR::MethodCallExpression *s) {
    return s;
}
const IR::Node *ReplaceVariables::postorder(IR::Expression *s) {
    auto expr = getOriginal<IR::Expression>();
    auto type = typeMap->getType((const IR::Node *)expr, true);

    if (typeMap->isLeftValue(expr)) {
        return s;
    }
    int bits = type->width_bits();

    auto decision = get_rnd_pct();
    if (decision < 0.5 && type->is<IR::Type_Bits>()) {
        // INFO(s);
        auto new_elt = new IR::Constant(new IR::Type_Bits(bits, false), 10);
        // INFO("Replacing " << s << " with " << new_elt);
        return new_elt;
    }
    return s;
}

const IR::P4Program *apply_replace(const IR::P4Program *program,
                                   P4PRUNER::PrunerConfig pruner_conf,
                                   bool first) {
    P4::ReferenceMap refMap;
    P4::TypeMap typeMap;
    const IR::P4Program *temp;

    std::initializer_list<Visitor *> passes;

    PassManager pass_manager(passes);
    // FIXME: This gives : Cannot find declaration for T
    //                      void extract<T>(out T hdr);

    if (first) {
        pass_manager.addPasses(
            {new P4::CreateBuiltins(), new P4::ResolveReferences(&refMap, true),
             new P4::ConstantFolding(&refMap, nullptr),
             new P4::InstantiateDirectCalls(&refMap),
             new P4::TypeInference(&refMap, &typeMap, false)});
    } else {
        pass_manager.addPasses(
            {new P4::TypeInference(&refMap, &typeMap, false)});
        if (&typeMap != nullptr) {
            pass_manager.addPasses({new P4::ClearTypeMap(&typeMap)});
        }
    }

    temp = program->apply(pass_manager);

    P4PRUNER::ReplaceVariables *replacer =
        new P4PRUNER::ReplaceVariables(&refMap, &typeMap);
    temp = temp->apply(*replacer);

    return temp;
} // namespace P4PRUNER

const IR::P4Program *replace_variables(const IR::P4Program *program,
                                       P4PRUNER::PrunerConfig pruner_conf) {
    int same_before_pruning = 0;
    int result;

    INFO("Replacing variables with literals");
    for (int i = 0; i < 5; i++) {
        auto temp = program;

        if (i == 0)
            temp = apply_replace(temp, pruner_conf, true);

        else
            temp = apply_replace(temp, pruner_conf, false);

        result = check_pruned_program(&program, temp, pruner_conf);

        if (result != EXIT_SUCCESS) {
            same_before_pruning++;
        } else {
            // successful run, reset short-circuit
            program = temp;
            same_before_pruning = 0;
        }
        if (same_before_pruning >= NO_CHNG_ITERS) {
            break;
        }
    }
    // Done pruning
    return program;
}

} // namespace P4PRUNER
