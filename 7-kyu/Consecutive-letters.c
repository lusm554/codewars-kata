// https://www.codewars.com/kata/5ce6728c939bf80029988b57/train/c

#include <stdbool.h>
#include <string.h> // strlen
#include <stdio.h>

bool consecutive(char *str_in) {
  // a - 97
  // z - 122
  int map[25] = {0};

  for (char *p = str_in; *p; p++) {
    if (map[*p-97] == 1) return false;
    map[*p-97] = 1;
  }
  
  int s = 0;
  for (int i = 1; i < 25; i++) {
    if (map[i-1]) {
      s = 1;
      continue;
    }
    
    if (s && (map[i-1] != map[i])) return false;
  }
  
  return true;
}
