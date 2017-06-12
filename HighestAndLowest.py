# https://www.codewars.com/kata/highest-and-lowest/train/python

def high_and_low(numbers):
    numblist = map(int, (numbers.split(' ')))
    return '%i %i' % (max(numblist), min(numblist))

print high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")#, "542 -214")
print high_and_low("1 -1")#, "1 -1")
print high_and_low("1 1")#, "1 1")
print high_and_low("-1 -1")#, "-1 -1")
print high_and_low("1 -1 0")#, "1 -1")
print high_and_low("1 1 0")#, "1 0")
print high_and_low("-1 -1 0")#, "0 -1")
print high_and_low("42")#, "42 42")