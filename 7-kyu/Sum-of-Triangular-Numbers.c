// https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/c

int sumTriangularNumbers(int n)
{
  if (n < 0) return 0;
  int sum = 0;
  int d = 1;
  
  // n - 01 03 06 10 = 1 + 3 + 6 + 10 = 20
  // i - 00 01 02 03 = 1 + 2 + 4 + 7  = 20
  
  for (int i = 0; i < n; i++) {
    sum += i + d;
    d += i + 1;
  }
  
  return sum;
}

