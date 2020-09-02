# A program asks user to enter a formula
# Print out whether the formula has the same number of opening an closing
# parentheses

def check(s): 
    brackets = ['()', '{}', '[]'] 
    while any(x in s for x in brackets): 
        for br in brackets: 
            s = s.replace(br, '') 
    return not s 
   
# Driver code 
s = input('Enter formula:\n')

print(s, "-", "Balanced" if check(s) else "Unbalanced") 
   
 
# VISIT: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

# {[]{()}} - Balanced
# ((()     - Unbalanced
