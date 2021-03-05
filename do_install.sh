#!/bin/bash

# exit when any command fails
set -e



# fetch submodules and update apt
echo "Initializing submodules..."
git submodule update --init --recursive
sudo apt-get update

SRC_DIR="$(pwd)"
MODULE_DIR="$(pwd)/modules"

echo "Installing P4C dependencies..."

# Install pip and python
sudo apt install -y python3
sudo apt install -y python3-pip
sudo apt install -y python3-setuptools

# Install the p4 compiler dependencies
sudo apt install -y bison \
                    build-essential \
                    cmake \
                    git \
                    flex \
                    libboost-dev \
                    libboost-graph-dev \
                    libboost-iostreams-dev \
                    libfl-dev \
                    libgc-dev \
                    libgmp-dev \
                    pkg-config

# This only works on Ubuntu 18+
sudo apt install -y libprotoc-dev protobuf-compiler

# install python packages using pip
pip3 install --user wheel
pip3 install --user pyroute2 ipaddr ply scapy

# only install the behavioral model if requested
# if [ "$INSTALL_BMV2" == "ON" ]; then
# echo "Behavioral model install selected."

# Install the behavioral model dependencies
# echo "Installing behavioral model dependencies."
# sudo apt install -y automake \
#     cmake \
#     libjudy-dev \
#     libgmp-dev \
#     libpcap-dev \
#     libboost-dev \
#     libboost-test-dev \
#     libboost-program-options-dev \
#     libboost-system-dev \
#     libboost-filesystem-dev \
#     libboost-thread-dev \
#     libevent-dev \
#     libtool \
#     flex \
#     bison \
#     pkg-config \
#     g++ \
#     libssl-dev \
#     libnanomsg-dev \
#     libgrpc-dev



# grab the toz3 extension for the p4 compiler
mkdir -p ${MODULE_DIR}/p4c/extensions

rm -rf {MODULE_DIR}/pruner
ln -sf ${MODULE_DIR}/pruner ${MODULE_DIR}/p4c/extensions/pruner


# ln -sf ${MODULE_DIR}/toz3 ${MODULE_DIR}/p4c/extensions/toz3

# build the p4 compiler
echo "Building P4C..."
cd ${MODULE_DIR}/p4c
mkdir -p build
cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j `getconf _NPROCESSORS_ONLN`
cd ../..

echo "Installing Gauntlet Python dependencies..."
# Install z3 locally
pip3 install --upgrade --user z3-solver
# Pytests for tests
pip3 install --upgrade --user pytest
# Run tests in parallel
pip3 install --upgrade --user pytest-xdist
# Python 3.6 compatibility
pip3 install --upgrade --user dataclasses



echo "Gauntlet installation completed successfully."
