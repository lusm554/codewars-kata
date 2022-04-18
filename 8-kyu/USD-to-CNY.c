// https://www.codewars.com/kata/5977618080ef220766000022/train/c

#include <math.h>
#include <stdio.h>

char *USD_to_CNY (long dollars, char *yuans)
{
  long double cny = 6.75;
  sprintf(yuans, "%.2Lf Chinese Yuan", (long double)dollars * cny);
  
	return yuans;
}

