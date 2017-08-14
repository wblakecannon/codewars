def get_last_digit(index):
    if index < 2:
        return index
    else:
        fib1, fib2 = 0, 1
        for i in range(1, index):
            fib1, fib2 = fib2, (fib1 + fib2) % 10
        return (fib2)


print get_last_digit(15)
print get_last_digit(193150)
print get_last_digit(300)
print get_last_digit(20001)
print get_last_digit(800)
print get_last_digit(1001)
print get_last_digit(100)
print get_last_digit(260)
print get_last_digit(1111)
print get_last_digit(1234)
print get_last_digit(99999)
print get_last_digit(10)
print get_last_digit(234)
print get_last_digit(193241)
print get_last_digit(79)
print get_last_digit(270)
