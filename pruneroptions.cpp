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
        "--validator_script", "file",
        [this](const char *arg) {
            validator_script = arg;
            return true;
        },
        "Path to the validation python script");

    registerOption(
        "--print_pruned", nullptr,
        [this](const char *) {
            print_pruned = true;
            return true;
        },
        "Whether to print out the pruned file to stdout");
}

} // namespace P4PRUNER
