// https://www.codewars.com/kata/58fa273ca6d84c158e000052/train/c

#include <stdint.h>

int digits(uint64_t n) {
  int c = 1;
  while ((int)(n /= 10) != 0) {
    c++;
  }
  
  return c;
}

