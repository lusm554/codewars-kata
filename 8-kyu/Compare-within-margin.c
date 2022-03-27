// https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/c

#include <stdlib.h>

int close_compare(int a, int b, int margin) {
  if (margin >= abs(a - b)) {
    return 0;
  }
  
  return a > b ? 1 : -1;
}

