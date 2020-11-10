#include "frontends/common/constantFolding.h"
#include "frontends/common/resolveReferences/resolveReferences.h"
#include "frontends/p4/createBuiltins.h"
#include "frontends/p4/directCalls.h"
#include "frontends/p4/simplify.h"
#include "frontends/p4/simplifyDefUse.h"
#include "frontends/p4/unusedDeclarations.h"

#include "compiler_pruner.h"
#include "prune_unused.h"
namespace P4PRUNER {


const IR::P4Program *apply_unused_decls(const IR::P4Program *program,
                                        P4PRUNER::PrunerConfig pruner_conf) {
    P4::ReferenceMap refMap;
    P4::TypeMap typeMap;
    const IR::P4Program *temp;

    PassManager pass_manager = {
        new P4::CreateBuiltins(), new P4::ResolveReferences(&refMap, true),
        new P4::ConstantFolding(&refMap, nullptr),
        new P4::InstantiateDirectCalls(&refMap),
        new P4::TypeInference(&refMap, &typeMap, false),
        // new P4::RemoveAllUnusedDeclarations(&refMap, false)};
        new PruneAllUnused(&refMap)};

    INFO("Applying custom RemoveAllUnusedDeclarations...");
    temp = program->apply(pass_manager);
    emit_p4_program(temp, pruner_conf.out_file_name);
    check_pruned_program(&program, temp, pruner_conf);

    return program;
}

const IR::P4Program *apply_compiler_passes(const IR::P4Program *program,
                                           P4PRUNER::PrunerConfig pruner_conf) {
    // this disables warning temporarily to avoid spam
    auto prev_action = P4CContext::get().getDefaultWarningDiagnosticAction();
    auto action = DiagnosticAction::Ignore;
    P4CContext::get().setDefaultWarningDiagnosticAction(action);
    INFO("\nPruning with compiler passes")

    // apply the compiler passes
    // right not this is just unused declarations
    program = apply_unused_decls(program, pruner_conf);

    // reset to previous warning
    P4CContext::get().setDefaultWarningDiagnosticAction(prev_action);

    return program;
}

} // namespace P4PRUNER
