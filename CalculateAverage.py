# https://www.codewars.com/kata/calculate-average/train/python

def find_average(array):
    if array == []:
        return 0
    else:
        return sum(array) / len(array)

print find_average([1, 2, 3])
print find_average([])
