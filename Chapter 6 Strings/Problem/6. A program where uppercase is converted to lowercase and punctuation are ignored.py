# A program asks user to enter string s,
# converts s to lowercase, remove all punctuation


s = input('Enter a string:')

# This will remove the uppercase and convert to lowercase
s1 = s.casefold() 

for c in ',.;:-?!()\'"!':
    s_new = s1.replace(c,'')

print(s_new)
