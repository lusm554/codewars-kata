# https://www.codewars.com/kata/58ca7afc92ce34dfa50001fa/train/python

import hashlib
import datetime
def geohash(dow, date=datetime.datetime.now()):
    date_text = date.strftime(f"%Y-%m-%d-{dow:.2f}")
    date_hash = hashlib.md5(date_text.encode('utf-8')).hexdigest()
    p1, p2 = '0.'+date_hash[:16], '0.'+date_hash[16:]
    hex2float10 = lambda x: sum(int(char, 16) * (16 ** -(i + 1)) for i, char in enumerate(x[2:]))
    p1, p2 = f"{hex2float10(p1):.6f}", f"{hex2float10(p2):.6f}"
    return [float(p1), float(p2)]
