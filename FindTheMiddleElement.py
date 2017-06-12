# https://www.codewars.com/kata/find-the-middle-element/train/python

def gimme(input_array):
    return input_array.index(sorted(input_array)[1])
    
print gimme([2, 3, 1])
