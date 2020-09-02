# A program asks user for a string and a letter and counts how many occurences
# there are of the letter in the string
# without using the count method


from collections import Counter

s  = input('Enter a string:')

counter = Counter(s)

print(counter['h'])


