# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python
from itertools import combinations
def longest_palindrome(s):
	if len(s) == 0: return 0
	for i in range(len(s), 0, -1):
		for j in range(len(s)-i+1):
			sub = s[j:j+i]
			if sub == sub[::-1]: return len(sub)
