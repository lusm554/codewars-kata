// https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/c

#include <stddef.h>

int diffsum(int *arr, size_t n)
{
  if ((int)n <= 1) return 0;
  
  int sum = 0;
  
  // bubble sort
  for (int i = 0; i < (int)n; i++) {
    for (int j = 0; j < i; j++) {
      if (arr[i] > arr[j]) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
      }
    } 
  }
  
  for (int i = 1; i < (int)n; i++) {
     sum += arr[i-1] - arr[i];
  }
  
  return sum;
}

