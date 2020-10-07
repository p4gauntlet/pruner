#ifndef _P4PRUNER_OPTIONS_H_
#define _P4PRUNER_OPTIONS_H_

#include "ir/ir.h"

#include "frontends/common/options.h"
#include "lib/options.h"

namespace P4PRUNER {

class PrunerOptions : public CompilerOptions {
  public:
    PrunerOptions();
    // output file
    cstring o_file = nullptr;
    bool emit_p4 = false;
    // input file is in CompilerOptions file
    bool do_rnd_prune = false;
    cstring validator_script = nullptr;
    bool print_pruned = true;
};

using P4PrunerContext = P4CContextWithOptions<PrunerOptions>;

} // namespace P4PRUNER

#endif /* _P4PRUNER_OPTIONS_H_ */
