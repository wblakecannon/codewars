# https://www.codewars.com/kata/square-n-sum/train/python

def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i*i
    return sum


print square_sum([1,2])
print square_sum([0, 3, 4, 5])