// https://www.codewars.com/kata/545993ee52756d98ca0010e1/train/c

#include <stdbool.h>
#include <stddef.h>

typedef bool (*Predicate)(int);

bool none(const int* arr, size_t size, Predicate fun)
{
  while (size--) if(fun(*arr++)) return false;
  return true;
}

