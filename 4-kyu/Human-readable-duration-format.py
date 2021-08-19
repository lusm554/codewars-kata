#!/usr/bin/env python3.9

# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(s):
    if s == 0: return 'now'
    sto = {
        'year': [31556952, lambda x: int(x/31556952)],
        'day': [86400, lambda x: int(x/86400)],
        'hour': [3600, lambda x: int(x/3600)],
        'minute': [60, lambda x: int(x/60)],
        'second': [1, lambda x: int(x/1)]
    }
    y, d, h, m = [0]*4
    res = {}
    s_res = ''
    for k, f in sto.items():
        cv = sto[k][1](s)
        if cv > 0:
            s -= sto[k][0]
            if cv > 1:
                s_res += f'{cv} {k} '
            else:
                s_res += f'{cv} {k}s '
    print(s_res)
    return ''

#-------------TEST-------------
class Test:
    def assert_equals(self, res, shouldbe):
        t = res == shouldbe
        print(t, '\n')
        return t

test = Test()

test.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
