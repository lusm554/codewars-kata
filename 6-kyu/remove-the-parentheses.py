# https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python

# more simple
def remove_parentheses(st):
    stack = list()
    current_list = list()
    for w in st:
        if w == '(':
            stack.append(current_list)    
            current_list = []
        elif w == ')':
            prev_list = stack.pop()
            prev_list.append(current_list)
            current_list = prev_list
        else:
            current_list.append(w)
    return ''.join(w for w in current_list if type(w) != list)

# too tricky
import re
def remove_parentheses(st):
    exp = '(' + '|'.join(map(re.escape, ['(', ')'])) + ')'
    st = re.split(exp, st)
    print(st)
    stack = list()
    current_list = list()
    for w in st:
        if w == '(':
            stack.append(current_list)    
            current_list = []
        elif w == ')':
            prev_list = stack.pop()
            prev_list.append(current_list)
            current_list = prev_list
        else:
            current_list.append(w)
    print(current_list)
    return ''.join(w for w in current_list if type(w) != list)
