# https://www.codewars.com/kata/iseven-bitwise-series/train/python

def is_even(number):
    if number == (number / 2) * 2:
        return True
    else:
        return False

print is_even(2)# True
