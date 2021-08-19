# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

def get_num(s):
    num_s = ''
    for i in range(len(s)-1, -1, -1):
        if not s[i].isnumeric(): break
        num_s = s[i] + num_s
    return num_s

def zeros_count(s):
    return len([z for z in s if int(z) == 0])

def increment_string(s):
    if s == '' or not str(s[-1]).isnumeric(): return s + '1';
    s_num = get_num(s)
    z_count = zeros_count(s_num)
    s = s[0:len(s)-len(s_num)]
    num = str(int(s_num) + 1)
    return s+'0'*z_count+num

# TEST
class Test:
    def assert_equals(self, res, expect):
        print(res==expect)

test = Test()
test.assert_equals(increment_string("foo"), "foo1")
test.assert_equals(increment_string("foobar001"), "foobar002")
test.assert_equals(increment_string("foobar1"), "foobar2")
test.assert_equals(increment_string("foobar00"), "foobar01")
test.assert_equals(increment_string("foobar99"), "foobar100")
test.assert_equals(increment_string("foobar099"), "foobar100")
test.assert_equals(increment_string(""), "1")
