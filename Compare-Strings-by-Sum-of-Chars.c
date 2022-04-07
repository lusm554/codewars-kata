// https://www.codewars.com/kata/576bb3c4b1abc497ec000065/train/c

#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>

bool compare(char *s1, char *s2) {
  int sm1 = 0, sm2 = 0;
  int skip1 = 0, skip2 = 0;
  
  if (s1 == NULL) {
    skip1 = 1;
  }
  
  if (s2 == NULL) {
    skip2 = 1;
  }
  
  if (!skip1) {
    for (char *p = s1; *p; p++) {
      if (!isalpha(*p)) {
        sm1 = 0;
        break;
      }
      sm1 += toupper(*p);
    }
  }
  
  if (!skip2) {
    for (char *p = s2; *p; p++) {
      if (!isalpha(*p)) {
        sm2 = 0;
        break;
      }
      sm2 += toupper(*p);
    } 
  }
  
  return sm1 == sm2;
}

