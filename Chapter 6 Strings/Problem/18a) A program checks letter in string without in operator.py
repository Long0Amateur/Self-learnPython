# A program asks user for a string and a letter and prints out whether or not
# the letter appears in the string
# without using the in operator

s = input('Enter a string:')


if s.isalpha():
    print(s,'Yout string starts with a letter.')

else:
    print(s,'Your string contains non-letter.')



