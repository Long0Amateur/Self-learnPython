# A program prints out each letter of the string double on a separate line
# If the input is HEY, the program will prints out
# HH
# EE
# YY

s = input('Enter a word:')

for i in range(len(s)):
    print(s[i]*2, end='\n')
