s = input('Enter a string\n')

# the total numbers of characters in the string

count = 0
for i in range(len(s)):
    if (s[i] != ' '): # Count each character except space
       count+=1
        
print('Total numbers of characters in the string:', count)

# the string repeated 10 times
print('The string is repeated 10 times:',s*10)

# thge first character of the string
print('The first character of the string:',s[0])

# the first three characters of the string
print('The first three character of the string:',s[:3])

# the last three characters of the string
print('The last three character of the string:',s[-3:])

# the string backwards
print('The string backwards:',s[::-1])

# the seventh character of the string if the string is long enough and a message otherwise
if len(s) >= 7:
    print('The seventh character of the string:',s[6])

else:
    print('The string is not long enough')

# the string with its first and last characters removed
print('The string with its first and last charactersd removed:',s[1:-1])

# the string in all caps
print('The string in all caps:',s.upper())

# the string with every a replaced an e
print('The string with every a replaced an e:',s.replace('a','e'))

# the string with every letter replace by a hyphen

print('The string with every letter replaced by a hyphen:',s.replace(s,'-'*len(s)))

