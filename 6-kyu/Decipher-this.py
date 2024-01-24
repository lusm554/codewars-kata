# https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python

def decipher_this(s):
    words = s.strip().split(' ')
    result = []
    for word in words:
        char_code = ''.join(filter(str.isdigit, word))
        word = word.replace(char_code, chr(int(char_code)))
        word = list(word)
        if len(word) >= 3:
            tmp = word[1]
            word[1] = word[-1]
            word[-1] = tmp
        result.append(''.join(word))
    return ' '.join(result)
