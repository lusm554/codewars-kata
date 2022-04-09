// https://www.codewars.com/kata/51c89385ee245d7ddf000001/train/c

#include <string.h>
#include <stdlib.h>

char* solution(int n)
{
  char *res = (char *)(malloc(sizeof(char) * 14));
  sprintf(res, "Value is %.5i", n);
  return res;
}

