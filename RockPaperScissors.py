# https://www.codewars.com/kata/rock-paper-scissors/train/python

def rps(p1, p2):
    if p1 == 'rock' and p2 == 'scissors':
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p2 == 'rock' and p1 == 'scissors':
        return "Player 2 won!"
    elif p2 == 'scissors' and p1 == 'paper':
        return "Player 2 won!"
    elif p2 == 'paper' and p1 == 'rock':
        return "Player 2 won!"
    else:
        return "Draw!"


print rps('rock', 'scissors')#, "Player 1 won!")
print rps('scissors', 'paper')#, "Player 1 won!")
print rps('paper', 'rock')#, "Player 1 won!")

print rps('scissors', 'rock')#, "Player 2 won!")
print rps('paper', 'scissors')#, "Player 2 won!")
print rps('rock', 'paper')#, "Player 2 won!")

print rps('rock', 'rock')#, 'Draw!')
print rps('scissors', 'scissors')#, 'Draw!')
print rps('paper', 'paper')#, 'Draw!')