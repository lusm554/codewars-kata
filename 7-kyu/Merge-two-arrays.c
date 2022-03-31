// https://www.codewars.com/kata/583af10620dda4da270000c5/train/c

#include <stddef.h>

void merge_arrays (size_t len_a, const int a[len_a], size_t len_b, const int b[len_b], int merged[len_a + len_b])
{
  int k = 0, i = 0, j = 0;
  int m_len = (int)(len_b + len_a);
  
  while (k < m_len) {
    if (i < len_a) {
      merged[k] = a[i];
      i++;
      k++;
    }
    
    if (j < len_b) {
      merged[k] = b[j];
      j++;
      k++;
    }
  }
}

