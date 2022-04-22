# https://www.codewars.com/kata/539de388a540db7fec000642/train/python

from datetime import datetime

def check_coupon(ent_code, corr_code, c_d, e_d):
    todate = lambda s: datetime.strptime(s, '%B %d, %Y')
    return (ent_code == corr_code and type(ent_code) == type(corr_code)) and \
            todate(c_d) <= todate(e_d)

