// https://www.codewars.com/kata/565b112d09c1adfdd500019c/train/c

#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

char *nth_char (size_t len, const char *const s[len], char *out)
{
  out = (char *)malloc(sizeof(char) * len);
  size_t i;
  
  for (i = 0; i < len; i++) {
    out[i] = s[i][i];
  }
  out[i] = '\0';
  
  return out;
}

