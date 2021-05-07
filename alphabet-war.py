# https://www.codewars.com/kata/alphabet-war

def alphabet_war(fight):
    count = 0
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    for i in fight:
        if i in left:
            count += left[i]
        elif i in right:
            count -= right[i]
    if count < 0:
        return "Right side wins!"
    if count > 0:
        return "Left side wins!"
    elif count == 0:
        return "Let's fight again!"


print(alphabet_war("z"))
print(alphabet_war("zdqmwpbs"))
print(alphabet_war("wq"))
print(alphabet_war("zzzzs"))
print(alphabet_war("wwwwww"))
