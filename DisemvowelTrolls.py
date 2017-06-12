'''
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from
the trolls'comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string
with all vowels removed.

For example, the string "This website is for losers LOL!" would become
"Ths wbst s fr lsrs LL!".
'''
def disemvowel(string):
    no_vowels = string
    vowels = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u')
    return ''.join([x for x in no_vowels if x not in vowels])

print(disemvowel("This website is for losers LOL!"))
