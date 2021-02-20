#!/usr/bin/env python3
import argparse
import pathlib
import os
import subprocess
import logging as log

SEED = 3370029442

FILE_DIR = pathlib.Path(__file__).parent.resolve()
REFERENCE_DIR = FILE_DIR.joinpath("references/")


EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def exec_process(cmd, *args, silent=False, **kwargs):
    log.debug("Executing %s ", cmd)
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, *args, **kwargs)
    if result.stdout:
        log.debug("Process output: %s", result.stdout.decode("utf-8"))
    if result.returncode != EXIT_SUCCESS and not silent:
        log.error("BEGIN %s", 40 * "#")
        log.error("Failed while executing:\n%s\n", cmd)
        log.error("Output:\n%s", result.stderr.decode("utf-8"))
        log.error("END %s", 40 * "#")

    return result


def main(args):

    COMPILER_BIN = args.compiler.absolute()
    VALIDATION_BIN = args.validation.absolute()
    PRUNER_BIN = args.pruner_path.absolute()
    P4_PROG = args.p4prog.absolute()

    if not os.access(COMPILER_BIN, os.X_OK):
        print("Please provide the path to a valid compiler binary")
        exit(EXIT_FAILURE)

    if not os.access(VALIDATION_BIN, os.X_OK):
        print("Please provide the path to a valid validation binary")
        exit(EXIT_FAILURE)

    if not os.access(PRUNER_BIN, os.X_OK):
        print("Please provide a valid path to the pruner")
        exit(EXIT_FAILURE)

    if not P4_PROG.is_file():
        print("Please provide the path to a valid p4 program")
        exit(EXIT_FAILURE)

    cmd_args = f"{PRUNER_BIN} --seed {SEED} --compiler-bin {COMPILER_BIN} --validation-bin {VALIDATION_BIN} {P4_PROG} --bug-type {args.type}"

    pruner_result = exec_process(cmd_args)

    if(pruner_result == EXIT_FAILURE):
        print("Error executing pruner,\n stderr :\n" +
              pruner_result.stderr.decode("utf-8"))
        print("\nstdout :\n" +
              pruner_result.stdout)
        exit(EXIT_FAILURE)

    PRUNED_FILE = pathlib.PosixPath(
        ".".join(str(P4_PROG).split('.')[:-1]) + '_stripped.p4')

    FILE_NAME = os.path.split(P4_PROG)[-1]

    ref_file = ".".join(
        str(FILE_NAME).split('.')[:-1]) + '_reference.p4'

    ref_folder = 'validation_bugs' if args.type == 'V' else 'crash_bugs'

    REFERENCE_FILE = REFERENCE_DIR.joinpath(f"{ref_folder}/{ref_file}")

    if REFERENCE_FILE.is_file():
        if os.system(f"diff {PRUNED_FILE} {REFERENCE_FILE}"):
            print("Test failed")
            exit(EXIT_FAILURE)
        else:
            print("Test passed")
            exit(EXIT_SUCCESS)
    else:
        print("Reference file not found")
        print(REFERENCE_FILE)
        exit(EXIT_FAILURE)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This file takes a p4 file along with a broken(bug-ridden) version of the p4c binary, and a validation binary, passes it to the pruner and then compares it to a reference file to test the working of the pruner.")
    parser.add_argument(
        "-c", "--compiler", dest='compiler', help="The path to the compiler binary", required=True, type=pathlib.Path)
    parser.add_argument(
        "-v", "--validation", dest='validation', help="The path to the validation binary", required=True, type=pathlib.Path)

    parser.add_argument(
        "-p4", "--p4prog", dest="p4prog", help="The path to the p4 program", required=True, type=pathlib.Path)
    parser.add_argument(
        "-p", "--pruner_path", dest='pruner_path', help="The path to the pruner", required=True, type=pathlib.Path)
    parser.add_argument(
        "-t", "--type", dest='type', help="Validation or Crash bug [V/C]", required=True, choices=['V', 'C'])

    parser.add_argument("-l", "--log_file", dest="log_file",
                        default="pruner_test.log", help="Specifies name of the log file.")

    parser.add_argument("-ll", "--log_level", dest="log_level", default="INFO",
                        choices=["CRITICAL", "ERROR", "WARNING",
                                 "INFO", "DEBUG", "NOTSET"],
                        help="The log level to choose.")
    args = parser.parse_args()

    log.basicConfig(filename=args.log_file,
                    format="%(levelname)s:%(message)s",
                    level=getattr(log, args.log_level),
                    filemode='w')
    stderr_log = log.StreamHandler()
    stderr_log.setFormatter(log.Formatter("%(levelname)s:%(message)s"))
    log.getLogger().addHandler(stderr_log)

    main(args)
