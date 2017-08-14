def last_fib_digit(index):
    if index < 2:
        return index
    else:
        fib1, fib2 = 0, 1
        for i in range(1, index):
            fib1, fib2 = fib2, (fib1 + fib2) % 10
        return (fib2)


print last_fib_digit(1)
print last_fib_digit(21)
print last_fib_digit(302)
print last_fib_digit(4003)
print last_fib_digit(50004)
print last_fib_digit(600005)
print last_fib_digit(7000006)
print last_fib_digit(80000007)
print last_fib_digit(900000008)
print last_fib_digit(1000000009)