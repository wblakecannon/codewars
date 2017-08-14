# https://www.codewars.com/kata/remove-exclamation-marks/train/python

def remove_exclamation_marks(s):
    return s.replace('!', '')

print remove_exclamation_marks("Hello World!")
print remove_exclamation_marks("Hello World!!!")
print remove_exclamation_marks("Hi! Hello!")
print remove_exclamation_marks("")
print remove_exclamation_marks("Oh, no!!!")