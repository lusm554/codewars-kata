// https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/c

#include <string.h>

void moveTen(char *str) {
  for (char *p = str; *p; p++) {
    int t = *p;
    for (int i = 0; i < 10; i++) {
      t++;
      if (t > 'z') {
        t = 'a';
      }
    }
    *p = t;
  }
}

