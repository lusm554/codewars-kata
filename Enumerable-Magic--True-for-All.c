// https://www.codewars.com/kata/54598d1fcbae2ae05200112c/train/c

#include <stdbool.h>
#include <stddef.h>

typedef bool (*Predicate)(int);

bool all(int* arr, size_t size, Predicate fun) {
  for (size_t i = 0; i < size; i++) if (!fun(arr[i])) return false;
  
  return true;
}

