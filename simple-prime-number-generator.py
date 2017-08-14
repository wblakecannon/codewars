# https://www.codewars.com/kata/simple-prime-number-generator/train/python

def generate_primes(x):
    pp = 2
    ps = [pp]
    while pp < int(x):
        pp += 1
        for a in ps:
            if pp % a == 0:
                break
            else:
                if pp not in ps:
                    ps.append(pp)
    return ps

print generate_primes(25)#, [2, 3, 5, 7, 11, 13, 17, 19, 23], "Not all primes on the list!")
print generate_primes(55)#, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], "Not all primes on the list!")
print generate_primes(150)#, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149], "Not all primes on the list!")