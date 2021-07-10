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

        if k == 'year':
            y = sto[k][1](s)
            if y > 0:
                s -= sto[k][0]
                if y > 1:
                    res['years'] = y
                else:
                    res['year'] = y
        elif k == 'day':
            d = sto[k][1](s)
            if d > 0:
                s -= sto[k][0]
                if s > 1:
                    res['days'] = d
                else:
                    res['day'] = d
        elif k == 'hour':
            h = sto[k][1](s)
            if h > 0:
                s -= sto[k][0]
                if h > 1:
                    res['hours'] = h
                else:
                    res['hour'] = h
        elif k == 'minute':

            m = sto[k][1](s)
            if m > 0:
                s -= sto[k][0]
                if m > 1:
                    res['minutes'] = m
                else:
                    res['minute'] = m
        elif k == 'second':
            s = sto[k][1](s)
            if s > 1:
                res['seconds'] = s
            else:
                res['second'] = s
    print(res)
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
