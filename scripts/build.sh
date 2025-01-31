#!/bin/bash
#
# Shell script to build the C ML project

set -ex

gcc src/c/main.c -o bin/main -std=c11 -lm
gcc src/c/n-tuple-input.c -o bin/n-tuple-inputs -std=c11 -lm
gcc src/c/gates.c -o bin/gates -std=c11 -lm

#bin/main
