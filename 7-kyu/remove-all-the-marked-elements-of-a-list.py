# https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python

class List:
  def remove_(self, integer_list, values_list):
    values_list = set(values_list)
    return [x for x in integer_list if x not in values_list]
