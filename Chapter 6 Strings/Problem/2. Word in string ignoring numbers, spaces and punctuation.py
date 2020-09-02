# A simple way to estimate the number of words in a string is to
# count the number of spaces in the string.

# A program that asks the user for a string and returns an estimate of
# how many words are in the string.


# Ignoring numbers, punctuation and whitespace

s =  'I am having a very nice day.'
s1 = 'I     am having  a   very  nice  23!@$      day.'

count = 1
for i in range(len(s)):
    if s[i] == ' ':
        count+=1

print(s)
print('Total words in the string are:',count)

import re

count = len(re.findall('[a-zA-Z_]+',s1))
#  [a-zA-Z_] = match any character beetwen lower and upper case.

print(s1)
print('Total words in the string are ( using regex.findall() ):',count)
