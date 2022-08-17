// https://www.codewars.com/kata/557341907fbf439911000022/train/cpp

#include <string>

std::string pattern(int n){
  std::string res;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= i; j++) {
      res += std::to_string(n - j);
    }
    if (i != n-1)
      res += '\n';
  }
  return res;
}
