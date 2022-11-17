#include <iostream>

int main() {
  int k = 0; // count of days in month
  int n = 0; // 1-7, day of week
  int dcnt = 0;

  if (!(std::cin >> n >> k)) {
    return 1;
  }
  
  for (int day = 0, i = 1; i < (n+k); ++i) {
    if (i < n) {
      std::cout << "   ";
    } else {
      ++day;
      if (day < 10) {
        std::cout << " " << day;
      } else {
        std::cout << day;
      }   
      std::cout << ' ';
    }   
    if (++dcnt == 7) {
      std::cout << std::endl;
      dcnt = 0;
    }   
  }
  std::cout << std::endl;

  return 0;
}

