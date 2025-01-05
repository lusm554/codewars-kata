# https://www.codewars.com/kata/53efc28911c36ff01e00012c/train/python

import sys
def count_calls(func, *args, **kwargs):
    def prof(frame, event, arg):
        nonlocal callcnt, lastreturn
        if event == 'call':
            callcnt += 1
        elif event == 'return':
            lastreturn = arg
    sys.setprofile(prof)
    callcnt = -1
    lastreturn = None
    func(*args, **kwargs)
    return callcnt, lastreturn
