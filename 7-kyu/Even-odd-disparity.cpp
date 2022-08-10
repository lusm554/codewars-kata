// https://www.codewars.com/kata/59c62f1bdcc40560a2000060/train/cpp

bool isdigit(std::string s)
{
  std::string::const_iterator it = s.begin();
  while (it != s.end() && std::isdigit(*it)) ++it;
  return !s.empty() && it == s.end();
}

int solve(std::vector<std::string>v){
  int even = 0, odd = 0;
  for (auto it = v.begin(); it != v.end(); it++) {
    if (isdigit(*it)) {
      if (std::stoi(*it) % 2 == 0) {
        even++;
      }
      else {
        odd++;
      }
    }
  }
  return even - odd; 
}
