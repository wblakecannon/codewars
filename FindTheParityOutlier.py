'''
You are given an array (which will have a length of at least 3, but could be
very large) containing integers. The array is either entirely comprised of
odd integers or entirely comprised of even integers except for a single
integer N. Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160
'''
def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 > 0:
            odds.append(i)
        if i % 2 == 0:
            evens.append(i)
    print "Evens: ", evens
    print "Odds: ", odds
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]

print find_outlier([2, 6, 8, 10, 3])
