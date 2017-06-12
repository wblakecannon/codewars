'''
The new "Avengers" movie has just been released! There are a lot of people at
the cinema box office standing in a huge line. Each of them has a single 100,
50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every
single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially
has no money and sells the tickets strictly in the order people follow in the
line?

Return YES, if Vasya can sell a ticket to each person and give the change.
Otherwise return NO.

###Examples:
### Python ###
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) 
# => NO. Vasya will not have enough money to give change to 100 dollars
'''
def tickets(people):
    bill25 = 0
    bill50 = 0
    bill100 = 0
    for i in people:
        if i == 25:
            bill25 += 1
        elif i == 50:
            if bill25 >= 1:
                bill25 -= 1
                bill50 += 1
            else:
                return "NO"
        elif i == 100:
            if bill25 >= 1 and bill50 >= 1:
                bill25 -= 1
                bill50 -= 1
                bill100 += 1
            elif bill25 >= 3:
                bill25 -= 3
                bill100 += 1
            else:
                return "NO"
    return "YES"

print tickets([25, 50, 25, 100])