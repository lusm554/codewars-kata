// https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca/train/c

#include <stddef.h>
#include <stdlib.h>

size_t catch_sign_change(const int *arr, size_t sz) {
  size_t c = 0;
  
  for (size_t i = 1; i < sz; i++) {
    if (arr[i-1] >= 0 && arr[i] < 0) c++;
    if (arr[i-1] < 0 && arr[i] >= 0) c++;
  }
  
  return c;
}

