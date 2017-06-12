# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        first = ''
        second = names[0]
    elif len(names) == 2:
        first = names[0]
        second = names[1]
    elif len(names) == 3:
        first = ', '.join(names[:2])
        second = names[-1]
    else:
        first = ', '.join(names[:2])
        second = '%d others' % (len(names) - 2)
    if first:
        return first + ' and ' + second + ' like this'
    else:
        return second + ' likes this'


print likes([])  # , 'no one likes this')
print likes(['Peter'])  # , 'Peter likes this')
print likes(['Jacob', 'Alex'])  # , 'Jacob and Alex like this')
print likes(['Max', 'John', 'Mark'])  # , 'Max, John and Mark like this')
# , 'Alex, Jacob and 2 others like this')
print likes(['Alex', 'Jacob', 'Mark', 'Max'])
