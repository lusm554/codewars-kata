// https://www.codewars.com/kata/57a62154cf1fa5b25200031e/train/c

char *alternateCase (char *s)
{
 for (char *p = s; *p; p++) {
   if (*p >= 'a' && *p <= 'z') {
      *p = (int)*p - 32;
   } else if (*p >= 'A' && *p <= 'Z') {
     *p = (int)*p + 32;
   }
 }
  
  return s;
}

