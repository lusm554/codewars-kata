#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Convert number to string representation
char *num2str(int n) {
  switch (n) {
    case 1:
      return "one";
    case 2:
      return "two";
    case 3:
      return "three";
    case 4:
      return "four";
    case 5:
      return "five";
    case 6:
      return "six";
    case 7:
      return "seven";
    case 8:
      return "eight";
    case 9:
      return "nine";
  };
  return "";
}

int main() {
  int a, b;
  scanf("%d\n%d", &a, &b);
  
  for (int i = a; i < b+1; i++) {
    if (i > 0 && i < 10) 
      printf("%s\n", num2str(i));

    if (i > 9 && i % 2 == 0)
      printf("even\n");
    
    if (i > 9 && i % 2 != 0)
      printf("odd\n");
  }

  return 0;
}

