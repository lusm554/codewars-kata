# https://www.codewars.com/kata/53fc954904a45eda6b00097f/train/python

import collections
class FilterList(collections.UserList):
    def __int_filter__(self, data):
        return [x for x in data if type(x) == int]
    
    def __compute__(self, condition):
        return [x for x in self.__int_filter__(self.data) if condition(x)]
    
    def even(self):
        return self.__compute__(lambda x: x % 2 == 0)
    
    def odd(self):
        return self.__compute__(lambda x: x % 2 != 0)
    
    def under(self, v):
        return self.__compute__(lambda x: x < v)
    
    def over(self, v):
        return self.__compute__(lambda x: x > v)
    
    def in_range(self, start, end):
        return self.__compute__(lambda x: x >= start and x <= end)

list = FilterList
