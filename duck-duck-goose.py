# https://www.codewars.com/kata/duck-duck-goose/train/python

def duck_duck_goose(players, goose):
    while len(players) < goose:
        goose = goose - len(players)
    return players[goose - 1].name

print duck_duck_goose(players, 1)#,  "a")
print duck_duck_goose(players, 3)#,  "c")
print duck_duck_goose(players, 10)#, "z")
print duck_duck_goose(players, 20)#, "z")
print duck_duck_goose(players, 30)#, "z")
print duck_duck_goose(players, 18)#, "g")
print duck_duck_goose(players, 28)#, "g")
print duck_duck_goose(players, 12)#, "b")
print duck_duck_goose(players, 2)#,  "b")
print duck_duck_goose(players, 7)#,  "f")