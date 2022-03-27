// https://www.codewars.com/kata/56fc55cd1f5a93d68a001d4e/train/c

#include <stddef.h>
#include <stdint.h>

uint32_t stairs_in_20(const int stairs[7][52]) {
  uint32_t sum = 0;

  for (int i = 0; i < 7; i++) {
    for (int j = 0; j < 52; j++) {
      sum += stairs[i][j];
    }
  }
  
  return sum * 20;
}

