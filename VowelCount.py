# https://www.codewars.com/kata/vowel-count/train/python

def getCount(inputStr):
    num_vowels = 0
    for i in inputStr:
        if i in "AEIOUaeiou":
            num_vowels = num_vowels + 1
    return num_vowels

print getCount('abracadabra') #5
