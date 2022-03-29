// https://www.codewars.com/kata/54599705cbae2aa60b0011a4/train/c

#include <stdbool.h>
#include <stddef.h>

typedef bool (*Predicate)(int);

bool one(const int* arr, size_t size, Predicate fun)
{
  if (!size) return false;
  
  int count = 0;
  for (int i = 0; i < (int)size; i++) {
    if (fun(arr[i]) && ++count > 1) return false;
  }
  
  return count == 1;
}

