#!/usr/bin/env python3
import argparse
import pathlib
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument(
    "--compiler", help="The path to the compiler binary", required=True, type=pathlib.Path)
parser.add_argument(
    "--validation", help="The path to the validation binary", required=True, type=pathlib.Path)

parser.add_argument(
    "--p4prog", help="The path to the p4 program", required=True, type=pathlib.Path)
parser.add_argument(
    "--pruner_path", help="The path to the pruner", required=True, type=pathlib.Path)
parser.add_argument(
    "--type", help="Validation or Crash bug [v/c]", required=True, choices=['V', 'C'])


args = parser.parse_args()
compiler_path = args.compiler.absolute()
validation_path = args.validation.absolute()

p4_prog_path = args.p4prog.absolute()
pruner_path = args.pruner_path.absolute()

if not os.access(compiler_path, os.X_OK):
    print(compiler_path)
    print("Please provide the path to a valid compiler binary")
    exit(1)

if not os.access(validation_path, os.X_OK):
    print(compiler_path)
    print("Please provide the path to a valid validation binary")
    exit(1)

if not os.access(pruner_path, os.X_OK):
    print(compiler_path)
    print("Please provide a valid path to the pruner")
    exit(1)


if not p4_prog_path.is_file():
    print("Please provide the path to a valid p4 program")
    exit(1)

seed = 3370029442
cmd_args = [
    str(pruner_path), "--seed", str(seed), "--compiler-bin", str(compiler_path),  "--validation-bin", str(validation_path), str(p4_prog_path), "--bug-type", args.type]

err = subprocess.run(cmd_args, capture_output=True).stderr
print(err)

pruned_file_path = pathlib.PosixPath(
    ".".join(str(p4_prog_path).split('.')[:-1]) + '_stripped.p4')

reference_file_path = pathlib.PosixPath(
    ".".join(str(p4_prog_path).split('.')[:-1]) + '_reference.p4')

if reference_file_path.is_file():
    if os.system(f"diff {pruned_file_path} {reference_file_path}"):
        print("Test failed")
        exit(1)
    else:
        print("Test passed")
        exit(0)
else:
    print("Reference file not found")
    exit(1)
