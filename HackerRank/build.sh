#!/bin/bash

# -Wall     – enables all compiler's warning messages.
# -Wextra   – enables some extra warning flags that are not enable by -Wall.
# -std      – defines certain standard.
# -pedantic – check standard.
clang -Wall -Wextra -std=c2x -pedantic $@

