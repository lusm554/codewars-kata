#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void calculate_the_maximum(int n, int k) {
  int maxAND = 0, maxOR = 0, maxXOR = 0;

  for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
      if (maxAND < (i & j) && (i & j) < k) {
        maxAND = i & j;
      }
      if (maxOR < (i | j) && (i | j) < k) {
        maxOR = i | j;
      }
      if (maxXOR < (i ^ j) && (i ^ j) < k) {
        maxXOR = i ^ j;
      }
    }
  }

  printf("%d\n", maxAND);
  printf("%d\n", maxOR);
  printf("%d\n", maxXOR);
}

int main() {
  int n, k;

  scanf("%d %d", &n, &k);
  calculate_the_maximum(n, k);

  return 0;
}

