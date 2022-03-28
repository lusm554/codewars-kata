// https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/c

int in_range(int i, int start, int end) {
  return i >= start && i <= end;
}

int is_letter(int c) {
  return in_range(c, 65, 90) || in_range(c, 97, 122);
}

int same_case (char a, char b) {
  int _a = (int)a;
  int _b = (int)b;
  
  if (!is_letter(_a) || !is_letter(_b)) return -1;
  
  if (in_range(_a, 65, 90) == in_range(_b, 65, 90)) return 1;
  
  return 0;
}

