// https://www.codewars.com/kata/5639bdcef2f9b06ce800005b/train/c

char *make_acronym (char *words, char *l)
{
  int j = 0;
  
  for (char *p = words; *p; p++) {
    if (*p == ' ' && *(p+1) != ' ') {
      l[j++] = *(p+1);
    }
    if (p == words) {
      l[j++] = *p;
    }
  }
  
  l[j] = '\0';
  
  return l; // return it
}

