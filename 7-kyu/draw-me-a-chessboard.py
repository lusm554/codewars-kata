# https://www.codewars.com/kata/56242b89689c35449b000059/train/python

def chess_board(r, c):
    return [[('O' if j % 2 == 0 else 'X') if i % 2 == 0 else ('X' if j % 2 == 0 else 'O') for j in range(c)] for i in range(r)]

