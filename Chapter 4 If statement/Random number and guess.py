#Guess-a-number game

from random import randint

x = randint(1,10)
y = eval(input('Enter your guess:'))
if y == x:
    print('You got it!')
else:
    print('Sorry. The number is',x)
