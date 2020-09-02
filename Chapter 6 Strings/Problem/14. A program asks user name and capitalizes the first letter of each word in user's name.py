# A program asks user to enter their name and
# capitalizes the first letter of each word of their name

import string

s = input('Enter your name:')

# This works for string with embedded apostrophes
print(string.capwords(s))
