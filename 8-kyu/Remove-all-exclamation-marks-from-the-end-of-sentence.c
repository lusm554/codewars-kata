// https://www.codewars.com/kata/57faece99610ced690000165/train/c

#include <string.h>

char *remove_marks (const char *in, char *out)
{
  int end = 0;
  int i = (int)strlen(in)-1;
  
  while (in[i--] == '!') {
    end++;
  }
  
  end = (int)strlen(in) - end;
 
  strncpy(out, in, end);
  out[end] = '\0';
  
  return out;
}

