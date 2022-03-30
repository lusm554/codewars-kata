// https://www.codewars.com/kata/5299413901337c637e000004/train/c

short missing_element (const short e[9])
{
  for (int i = 0; i < 9; i++) {
    int is_ok = 0;
    for (int j = 0; j < 9; j++) {
      if (i == e[j]) {
        is_ok = 1;
        break;
      }
    }
    
    if (!is_ok) return i;
  }
  
  return 9;
}

