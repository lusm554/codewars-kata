// https://www.codewars.com/kata/59859f435f5d18ede7000050/train/cpp

#include <vector>
#include <string>
#include <bitset>

std::vector<std::string> word_to_bin(std::string word) {
  std::vector<std::string> res;
  for (auto c : word)
    res.push_back(std::bitset<8>(c).to_string());
  return res;
}
