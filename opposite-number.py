# https://www.codewars.com/kata/opposite-number/train/python

def opposite(number):
    if number < 0:
        return abs(number)
    else:
        return number - number - number

print opposite(1) #,-1)

