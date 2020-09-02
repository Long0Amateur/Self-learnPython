# A program to deterimine if the word is a palindrome or not.
# A palindrome is a word that reads the same backwards as forwards
# (e.g. mom, level, racecar, noon)

# Visit https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

def check_palindrome(s):
    return s == s[::-1]

s = input('Enter a word:')

ans = check_palindrome(s)

if ans:
    print(s,'is a palindrome')

else:
    print(s,'is not a palindrome')
