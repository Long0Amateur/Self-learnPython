# A program creates a random assortment of 100 letters

from random import choice

alphabet = 'abcdefghijklmnopqrstuvwxyz'

s = ''.join( choice(alphabet) for i in range(100) )

print(s)
