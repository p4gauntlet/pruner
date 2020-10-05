#include <fstream>

#include "frontends/common/parseInput.h"
#include "frontends/p4/toP4/toP4.h"
#include "ir/ir.h"
#include "lib/nullstream.h"
#include "lib/cstring.h"

#include "pruner.h"
#include "pruneroptions.h"

cstring remove_extension(cstring filename) {
    // find the last dot
    const char *last_dot = filename.findlast('.');
    // there is no dot in this string, just return the full name
    if (not last_dot) {
        return filename;
    }
    // otherwise get the index, remove the dot
    size_t idx = (size_t)(last_dot - filename);
    return filename.substr(0, idx);
}

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

        // if the emit flag is enabled, also emit the new p4 version
        if (options.emit_p4) {
            auto stripped_name = remove_extension(options.file);
            printf("%s\n", stripped_name);
            auto p4_ostream = openFile(stripped_name + "_stripped.p4", false);
            P4::ToP4 *top4 = new P4::ToP4(p4_ostream, false);
            program->apply(*top4);
        }
    }

    return ::errorCount() > 0;
}
