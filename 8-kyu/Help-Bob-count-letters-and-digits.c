// https://www.codewars.com/kata/5738f5ea9545204cec000155/train/c

#include <stddef.h>
#include <string.h>

size_t count_letters_and_digits(const char *input) {
  int n = strlen(input);
  int s = 0;
  
  for (int i = 0; i < n; i++) {
    if ((int)(input[i]) >= 97 && (int)(input[i]) <= 122 || 
        (int)(input[i]) >= 65 && (int)(input[i]) <= 90  ||
        (int)(input[i]) >= 48 && (int)(input[i]) <= 57 ) {
      s++;
    }
  }
    
  return (size_t)s;
}

