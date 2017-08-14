# https://www.codewars.com/kata/help-mrs-jefferson/train/python

def shortest_arrang(n):
    student_range = reversed(range(n))

    return student_range

print shortest_arrang(10)#,[4, 3, 2, 1])
print shortest_arrang(14)#,[5, 4, 3, 2])
print shortest_arrang(16)#,[-1])
print shortest_arrang(22)#,[7, 6, 5, 4])
print shortest_arrang(65)#,[33, 32])

