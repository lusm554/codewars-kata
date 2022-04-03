// https://www.codewars.com/kata/5f55ecd770692e001484af7d/train/c

#include <stddef.h>

void mirror(const int *d, size_t n, int *res) {
  for (size_t i = 0; i < n; i++) {
    res[i] = d[i];
  }

  for (size_t i = 0; i < n; i++) {
    for (size_t j = i; j < n; j++) {
      if (res[i] > res[j]) {
        int t = res[i];
        res[i] = res[j];
        res[j] = t;
      }
    }    
  }
  
  for (size_t i = n, j = n-2; i < n*2; i++) {
    res[i] = res[j--];
  }
}

