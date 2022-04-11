// https://www.codewars.com/kata/53697be005f803751e0015aa/train/c

#include <stdlib.h> // malloc
#include <string.h> // strlen

// probably the not best option
#define vowels (char[]){'a', 'e', 'i', 'o', 'u'}

char *encode(const char *string) {
  char *res = malloc(sizeof(char) * strlen(string) * 1.1);
  strcpy(res, string);

  for (char *p = res; *p; p++) {
    for (int i = 0; i < 5; i++) {
      if (*p == vowels[i]) {
        *p = (i+1)+'0';
      }
    }
  }
  return res;
}

char *decode(const char *string) {
  char *res = malloc(sizeof(char) * strlen(string)* 1.1);
  strcpy(res, string);
  
  for (char *p = res; *p; p++) {
    for (int i = 0; i < 5; i++) {
      if (*p == (i+1)+'0') {
        *p = vowels[i];
      }
    }
  }
  
  return res;
}

