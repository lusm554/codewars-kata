# https://www.codewars.com/kata/5296455e4fe0cdf2e000059f/train/python

def calculate(num1, op, num2): 
    try:
        match op:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
            case '/':
                return num1 / num2
    except ZeroDivisionError:
        return
