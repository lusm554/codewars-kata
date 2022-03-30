// https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/c

int minSum(int arr[], int n)
{
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (arr[i] > arr[j]) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
      }
    }
  }
  
  int sum = 0;
  
  for (int i = 0, j = n-1; i < n/2; i++, j--) {
    sum += arr[i]*arr[j];
  }
  
  return sum;
}

