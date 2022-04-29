# https://www.codewars.com/kata/586538146b56991861000293/train/python

def to_nato(w):
    codes = {
        'a' : "Alfa",
        'b' : "Bravo",
        'c' : "Charlie",
        'd' : "Delta",
        'e' : "Echo",
        'f' : "Foxtrot",
        'g' : "Golf",
        'h' : "Hotel",
        'i' : "India",
        'j' : "Juliett",
        'k' : "Kilo",
        'l' : "Lima",
        'm' : "Mike",
        'n' : "November",
        'o' : "Oscar",
        'p' : "Papa",
        'q' : "Quebec",
        'r' : "Romeo",
        's' : "Sierra",
        't' : "Tango",
        'u' : "Uniform",
        'v' : "Victor",
        'w' : "Whiskey",
        'x' : "Xray",
        'y' : "Yankee",
        'z' : "Zulu",
        '0' : "Zero",
        '1' : "One",
        '2' : "Two",
        '3' : "Three",
        '4' : "Four",
        '5' : "Five",
        '6' : "Six",
        '7': "Seven",
        '8' : "Eight",
        '9' : "nine"
    }
    s = [codes[i] if i in codes else i if i in ',.!?' else '' for i in w.replace(' ', '').lower()]

    return ' '.join(s)
    
