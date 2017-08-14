# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no/train/python

def bool_to_word(bool):
    if bool == True:
        return 'Yes'
    else:
        return 'No'

print bool_to_word(True) #Yes
print bool_to_word(False) #No
