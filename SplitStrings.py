# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(s):
    if len(s) == 0:
        return []
    elif len(s) % 2 != 0:
        s = s +'_'
        return map(''.join, zip(*[iter(s)]*2))
    elif len(s) % 2 == 0:
        return map(''.join, zip(*[iter(s)]*2))
    else:
        s = s + '_'
        return map(''.join, zip(*[iter(s)]*2))



print solution("asdfadsf")#['as', 'df', 'ad', 'sf']
print solution("asdfads")#['as', 'df', 'ad', 's_']
print solution("")# []
print solution("x")# [x_]