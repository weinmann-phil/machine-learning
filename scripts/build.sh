#!/bin/bash
#
# Shell script to build the C ML project

set -ex

gcc src/c/main.c -o bin/main -std=c11 -lm
#clang -Wall -Wextra -o main main.c
