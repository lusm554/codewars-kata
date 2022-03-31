// https://www.codewars.com/kata/5590961e6620c0825000008f/train/c

#include <string.h>
#include <stdio.h>

char *swap_case (const char *s, char *sw)
{
	*sw = '\0'; // write to swapped
    
  for (int c = 0; c < (int)strlen(s); c++) {
    if (s[c] >= 'a' && s[c] <= 'z') {
      sw[c] = s[c] - 32;
    } else if (s[c] >= 'A' && s[c] <= 'Z') {
      sw[c] = s[c] + 32;
    } else {
      sw[c] = s[c];
    }
  }
  
	return sw; // return it
}
