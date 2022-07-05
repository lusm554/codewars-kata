// https://www.codewars.com/kata/57b68bc7b69bfc8209000307/train/c

#include <stddef.h> // size_t
#include <math.h> // round

int average(const int *values, size_t count)
{
  int sum = 0;
  int i = 0;

  loop:
    sum += values[i];
    i++;

    if (i < (int)count)
      goto loop;

  return round((float)sum/(float)count);
}

