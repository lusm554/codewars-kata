// https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/c

#include <stdlib.h>
#include <string.h>

char *remove_url_anchor(char *url_in) {
  char *res = malloc(strlen(url_in) * sizeof(char));
  int j = 0;
  
  for (char *p = url_in; *p; p++) {
    if (*p == '#') {
      break;
    }
    res[j++] = *p;
  }
  res[j] = '\0';

  return res;
}

