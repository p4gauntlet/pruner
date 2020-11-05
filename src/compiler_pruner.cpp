#include "frontends/common/constantFolding.h"
#include "frontends/common/resolveReferences/resolveReferences.h"
#include "frontends/p4/createBuiltins.h"
#include "frontends/p4/directCalls.h"
#include "frontends/p4/simplify.h"
#include "frontends/p4/simplifyDefUse.h"
#include "frontends/p4/unusedDeclarations.h"

#include "compiler_pruner.h"
#include "pruner_util.h"

namespace P4PRUNER {

const IR::P4Program *apply_def_use(const IR::P4Program *program,
                                   P4PRUNER::PrunerOptions options,
                                   int required_exit_code) {
    P4::ReferenceMap refMap;
    P4::TypeMap typeMap;
    const IR::P4Program *temp;

    PassManager pass_manager = {new P4::CreateBuiltins(),
                                new P4::ResolveReferences(&refMap, true),
                                new P4::ConstantFolding(&refMap, nullptr),
                                new P4::InstantiateDirectCalls(&refMap),
                                new P4::TypeInference(&refMap, &typeMap, false),
                                new P4::SimplifyDefUse(&refMap, &typeMap)};

    INFO("Applying SimplifyDefUse...");
    temp = program->apply(pass_manager);
    emit_p4_program(temp, STRIPPED_NAME);
    if (compare_files(temp, program)) {
        INFO("Skipped RemoveAllUnusedDeclarations");
        return temp;
    }

    if (get_exit_code(STRIPPED_NAME, options.validator_script) ==
        required_exit_code) {
        INFO("PASSED SimplifyDefUse: Reduced by " << measure_pct(program, temp)
                                                  << " %")
        program = temp;
    }
    return program;
}

const IR::P4Program *apply_control_flow_simpl(const IR::P4Program *program,
                                              P4PRUNER::PrunerOptions options,
                                              int required_exit_code) {
    P4::ReferenceMap refMap;
    P4::TypeMap typeMap;
    const IR::P4Program *temp;

    PassManager pass_manager = {new P4::CreateBuiltins(),
                                new P4::ResolveReferences(&refMap, true),
                                new P4::InstantiateDirectCalls(&refMap),
                                new P4::TypeInference(&refMap, &typeMap, false),
                                new P4::SimplifyControlFlow(&refMap, &typeMap)};

    INFO("Applying SimplifyControlFlow...");
    temp = program->apply(pass_manager);
    emit_p4_program(temp, STRIPPED_NAME);
    if (compare_files(temp, program)) {
        INFO("Skipped RemoveAllUnusedDeclarations");
        return temp;
    }

    if (get_exit_code(STRIPPED_NAME, options.validator_script) ==
        required_exit_code) {
        INFO("PASSED SimplifyControlFlow: Reduced by "
             << measure_pct(program, temp) << " %")
        program = temp;
    }
    return program;
}

const IR::P4Program *apply_unused_decls(const IR::P4Program *program,
                                        P4PRUNER::PrunerOptions options,
                                        int required_exit_code) {
    P4::ReferenceMap refMap;
    P4::TypeMap typeMap;
    const IR::P4Program *temp;

    PassManager pass_manager = {
        new P4::CreateBuiltins(),
        new P4::ResolveReferences(&refMap, true),
        new P4::ConstantFolding(&refMap, nullptr),
        new P4::InstantiateDirectCalls(&refMap),
        new P4::TypeInference(&refMap, &typeMap, false),
        new P4::RemoveAllUnusedDeclarations(&refMap, false)};

    INFO("Applying RemoveAllUnusedDeclarations...");
    temp = program->apply(pass_manager);
    emit_p4_program(temp, STRIPPED_NAME);
    if (compare_files(temp, program)) {
        INFO("Skipped RemoveAllUnusedDeclarations");
        return temp;
    }
    if (get_exit_code(STRIPPED_NAME, options.validator_script) ==
        required_exit_code) {
        INFO("PASSED RemoveAllUnusedDeclarations: Reduced by "
             << measure_pct(program, temp) << " %")
        program = temp;
    } else {
        INFO("FAILED RemoveAllUnusedDeclarations");
    }
    return program;
}

const IR::P4Program *apply_compiler_passes(const IR::P4Program *program,
                                           P4PRUNER::PrunerOptions options,
                                           int required_exit_code) {
    // this disables warning temporarily to avoid spam
    auto prev_action = P4CContext::get().getDefaultWarningDiagnosticAction();
    auto action = DiagnosticAction::Ignore;
    P4CContext::get().setDefaultWarningDiagnosticAction(action);

    // apply the compiler passes
    // program = apply_def_use(program, options, required_exit_code);
    program = apply_unused_decls(program, options, required_exit_code);
    // program = apply_control_flow_simpl(program, options, required_exit_code);

    // reset to previous warning
    P4CContext::get().setDefaultWarningDiagnosticAction(prev_action);

    return program;
}

} // namespace P4PRUNER
