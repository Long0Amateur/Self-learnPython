# A program picks a random character from a string

from random import choice

s = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

for i in range(50):
    print(i, choice(s),end= '\n')
