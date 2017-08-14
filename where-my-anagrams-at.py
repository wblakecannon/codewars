# https://www.codewars.com/kata/where-my-anagrams-at/train/python

def anagrams(word, words):
    is_match = sorted(word)
    return [w for w in words if is_match == sorted(w)]
#    return (word_list == words_list)


print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])#, ['aabb', 'bbaa'])
print anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])#, ['carer', 'racer'])