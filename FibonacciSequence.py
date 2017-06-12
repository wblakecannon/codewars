def get_last_digit(index):
    x = [1, 1]
    for i in xrange(index - 2):
        x.append(x[-1] + x[-2])
    fibstr = ', '.join(str(y) for y in x)
    return fibstr[-1]

print get_last_digit(193150)
# print get_last_digit(300)
# print get_last_digit(20001)
# print get_last_digit(800)
# print get_last_digit(1001)
# print get_last_digit(100)
# print get_last_digit(260)
# print get_last_digit(1111)
# print get_last_digit(1234)
# print get_last_digit(99999)
# print get_last_digit(10)
# print get_last_digit(234)
# print get_last_digit(193241)
# print get_last_digit(79)
# print get_last_digit(270)
