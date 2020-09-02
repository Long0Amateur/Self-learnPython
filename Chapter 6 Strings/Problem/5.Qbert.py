# A program asks user to enter a string, modify its string
# by adding asterisk to second character and three exclamation points attached
# to the end of string

s = input('Enter your string:\n')

s1 = s.replace(s[1],'*')

new_string = s1 + '!'*3

print(new_string)
