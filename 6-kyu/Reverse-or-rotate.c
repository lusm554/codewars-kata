// https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/c

#include <stdlib.h> // malloc
#include <stdio.h> // printf
#include <string.h> // strlen

char* revrot(char* s, int sz) {
  int len = (int)strlen(s);
  
  if (sz <= 0 || len == 0 || sz > len) return "";
  
  char *res = malloc(sizeof(char) * (len/sz) * sz);
  int c = len / sz;
  
//   printf("\n\ns: \"%s\", len: %lu, sz: %i, chunks: %d\n\n", s, strlen(s), sz, c);
  
  for (int i = 0; i < c; i++) {
    int sum = 0;
    char *ch = malloc(sizeof(char) * sz);
    strncpy(ch, s + sz * i, sz);
    
    for (int j = 0; j < sz; j++) {
      sum += ch[j] * ch[j] * ch[j];
    }
    
//     printf("s: %s, ch: %s, i: %i, sum: %i\n", s, ch, i, sum);
    if (sum % 2 == 0) { // reverse
      strrev(ch);
      strcat(res, ch);
    } else { // rotate
      char *temp = malloc(sizeof(char)*sz);
      int tempc = ch[0];
      for (int i = 0; i < sz-1; i++)
        temp[i] = ch[i+1];
      temp[sz-1] = tempc;
      strcat(res, temp);
    }
    free(ch);
  }
  
  return res;
}

