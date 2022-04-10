// https://www.codewars.com/kata/577b9960df78c19bca00007e/train/c

#include <stdlib.h> // abs

int nth_digit (int n, int i)
{
  if (i < 1) return -1;

  n = abs(n);
  while (n/10 > -1) {
    if(i-- == 1) {
      return n % 10;
    }
    n /= 10;
  }
  
  return 0;
}

