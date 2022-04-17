#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int size(const int num) {
  return num * 2 - 1;
}

int main() {
  int n;

  printf("Number: "); // delete
  scanf("%d", &n);

  int row_size = size(n);
  
  for (int i = 0; i < row_size; i++) {
    for (int j = 0; j < row_size; j++) {
      int curr_num;

      if (i < row_size / 2) {
        curr_num = n - i;
      } else {
        curr_num = i - n;
      }
      
      printf("%d ", curr_num);
    }
    printf("\n");
  }

  return 0;
}

