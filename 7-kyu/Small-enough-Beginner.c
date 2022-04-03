// https://www.codewars.com/kata/57cc981a58da9e302a000214/train/c

#include <stdbool.h>
#include <stddef.h>

bool small_enough(int *arr, size_t len, int limit) {
  for (size_t i = 0; i < len; i++) {
    if (arr[i] > limit) return false;
  }
  
  return true;
}

