// https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/c

#include <stdlib.h>

int *reverse_list(const int *in, size_t len) {
  int *out = malloc(len * sizeof(int));
  
  for (int i = 0; i < len; i++) out[i] = in[len-i-1];
  
  return out;
}

