#include <stdio.h>

int max_of_four(int a, int b, int c, int d) {
  int arr[] = {a, b, c, d};

  for (int i = 0; i < 4; i++)
    for (int j = 0; j < i; j++)
      if (arr[i] < arr[j]) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
      }

  return arr[3];
}

int main() {
  int a, b, c, d;
  scanf("%d %d %d %d", &a, &b, &c, &d);
  int ans = max_of_four(a, b, c, d);
  printf("%d", ans);

  return 0;
}

