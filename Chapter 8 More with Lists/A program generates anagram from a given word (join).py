# A program creates an anagram of a given word

from random import shuffle
word = input('Enter a word:')

# list = turn a  string s into a list L 
letter_list = list(word)

# shuffle = randomly arrange characters in given list
shuffle(letter_list)

# join = turn the list back into string
anagram = ''.join(letter_list)

print(anagram)
