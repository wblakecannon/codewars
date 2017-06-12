# https://www.codewars.com/kata/find-multiples-of-a-number/train/python

def find_multiples(integer, limit):
    multiples = []
    while limit:
        integer, limit = limit, (integer % limit)
        print integer
    return multiples

print find_multiples(5, 25)