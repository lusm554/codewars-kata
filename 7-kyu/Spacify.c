// https://www.codewars.com/kata/57f8ee485cae443c4d000127/train/c

#include <stdlib.h>
#include <string.h>

char *spacify(const char *str_in) {
  size_t len = strlen(str_in);
  char *new = malloc(len*2*sizeof(char));
  
  for (size_t i = 0; i < len; i++) {
    new[2*i] = str_in[i];
    
    if (i != len - 1) {
      new[2*i + 1] = ' ';
    }
  }
  new[len*2-1] = '\0';
  
  return new;
}

