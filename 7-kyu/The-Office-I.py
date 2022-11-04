# https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1/solutions/python

def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss] ) / len(meet) <= 5 else 'Nice Work Champ!'

