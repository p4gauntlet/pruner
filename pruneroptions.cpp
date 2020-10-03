#include "pruneroptions.h"

namespace P4PRUNER {

PrunerOptions::PrunerOptions() {
    registerOption(
        "--output", "file",
        [this](const char *arg) {
            o_file = arg;
            return true;
        },
        "The translated Z3 file.");
    registerOption(
        "--emit_p4", nullptr,
        [this](const char *) {
            emit_p4 = true;
            return true;
        },
        "Whether to emit a p4 file after.");
    registerOption(
        "--prune", nullptr,
        [this](const char *) {
            do_rnd_prune = true;
            return true;
        },
        "Enable random removal of statements.");
}

} // namespace P4PRUNER
