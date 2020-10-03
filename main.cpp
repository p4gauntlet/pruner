#include <fstream>

#include "frontends/common/parseInput.h"
#include "frontends/p4/toP4/toP4.h"

#include "ir/ir.h"
#include "toz3Options.h"
#include "pruner.h"



int main(int argc, char *const argv[]) {

    AutoCompileContext autoP4toZ3Context(new P4TOZ3::P4toZ3Context);
    auto &options = P4TOZ3::P4toZ3Context::get().options();
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


                PRUNER::Pruner *pruner = new PRUNER::Pruner();
                program = program->apply(*pruner);


                P4::ToP4 *after = new P4::ToP4(&std::cout, false);
    

                program->apply(*after);



        }
    

    return ::errorCount() > 0;
}

