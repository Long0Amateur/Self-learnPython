# Returns True if every character of the string is a letter

s = input('Enter a string:')

if s[0].isalpha():
    print('Your string starts with a letter')

if not s.isalpha():
    print('Your string contains a non-letter.')
    
