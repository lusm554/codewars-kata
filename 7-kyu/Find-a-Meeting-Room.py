# https://www.codewars.com/kata/57f604a21bd4fe771b00009c/train/python

def meeting(rooms):
    try:
        return rooms.index('O')
    except ValueError:
        return "None available!"

