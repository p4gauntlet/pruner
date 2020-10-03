#include <fstream>

#include "frontends/common/parseInput.h"
#include "frontends/p4/toP4/toP4.h"

#include "ir/ir.h"
#include "pruner.h"
#include "pruneroptions.h"

int main(int argc, char *const argv[]) {
    AutoCompileContext autoP4toZ3Context(new P4PRUNER::P4PrunerContext);
    auto &options = P4PRUNER::P4PrunerContext::get().options();
    options.langVersion = CompilerOptions::FrontendVersion::P4_16;

    if (options.process(argc, argv) != nullptr) {
        options.setInputFile();
    }
    if (::errorCount() > 0)
        return 1;

    if (options.file == nullptr) {
        options.usage();
        return 1;
    }

    const IR::P4Program *program = nullptr;

    program = P4::parseP4File(options);

    if (program != nullptr && ::errorCount() == 0) {
        // P4::ToP4 *before = new P4::ToP4(&std::cout, false);
        // program->apply(*before);

        P4PRUNER::Pruner *pruner = new P4PRUNER::Pruner();
        program = program->apply(*pruner);

        P4::ToP4 *after = new P4::ToP4(&std::cout, false);

        program->apply(*after);
    }

    return ::errorCount() > 0;
}
