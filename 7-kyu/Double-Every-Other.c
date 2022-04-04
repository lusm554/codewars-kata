// https://www.codewars.com/kata/5809c661f15835266900010a/train/c

#include <stddef.h>

void double_every_other (size_t len, int arr[len])
{
  for (size_t i = 0; i < len; i++) {
    if (i % 2 != 0) {
      arr[i] = arr[i] * 2;
    }
  }
}

