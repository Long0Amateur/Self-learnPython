# A program asks user for a string and returns a random anagram of the string

import random

def anagram(value):
    '''Returns random anagram of given value'''
    return ''.join(random.sample(value, len(value)))

s = input('Enter a string:')
print(anagram(s))
