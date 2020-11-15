#include "pruner_options.h"

namespace P4PRUNER {

PrunerOptions::PrunerOptions() {
    registerOption(
        "--emit-p4", nullptr,
        [this](const char *) {
            emit_p4 = true;
            return true;
        },
        "Whether to emit a p4 file after.");
    registerOption(
        "--config", "file",
        [this](const char *arg) {
            config_file = arg;
            return true;
        },
        "A configuration file with hints for validation.");
    registerOption(
        "--validation-bin", "file",
        [this](const char *arg) {
            validation_bin = arg;
            return true;
        },
        "Path to the validation python script");
    registerOption(
        "--working-dir", "file",
        [this](const char *arg) {
            working_dir = arg;
            return true;
        },
        "Where to place ephemeral files.");
    registerOption(
        "--print-pruned", nullptr,
        [this](const char *) {
            print_pruned = true;
            return true;
        },
        "Whether to print out the pruned file to stdout");
    registerOption(
        "--seed", "seed",
        [this](const char *arg) {
            seed = arg;
            return true;
        },
        "The seed for the random program. "
        "If no seed is provided we generate our own.");
}

} // namespace P4PRUNER
