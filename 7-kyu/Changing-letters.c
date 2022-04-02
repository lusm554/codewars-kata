// https://www.codewars.com/kata/5831c204a31721e2ae000294/train/c

char *capitalize_vowels (char *s)
{
  // a, e, i, o, u
  for (int i = 0; s[i] != '\0'; i++) {
    if (s[i] == 'a' || s[i] == 'o' ||
        s[i] == 'e' || s[i] == 'i' ||
        s[i] == 'i' || s[i] == 'u') {
      s[i] = toupper(s[i]);
    }
  }
  
	return s;
}

