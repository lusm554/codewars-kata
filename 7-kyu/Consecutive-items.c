// https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/c

#include <stdbool.h>
#include <stddef.h>

bool consecutive(const int *arr, size_t n, int a, int b) {
  for (size_t i = 1; i < n; i += 1) {
    if (arr[i-1] + arr[i] == a + b) return true;
  }
  
  return false;
}

