# A program that asks the user to enter a word and prints out whether that word
# contains any vowels, counts the vowel, list the vowels .

# Visit: https://www.geeksforgeeks.org/python-count-display-vowels-string/

# This program combines the string way and dictionary way 

def check_string(s, v): # s = string, v = vowels

    final = [each for each in s if each in v] # This is called comprehension
    
    # This will print out how many vowels in the word.
    print(s, 'has', len(final),'vowels')
    
    # This will print out the vowels in the word.
    print(final) 

def check_dictionary(s,v):      
    # casefold has been used to ignore cases (i.e: uppercase)
    s = s.casefold()

    # This will print out the number of vowels in the word
    # To do that, forms a dictionary with key as a vowel and the value as 0
    count = {}.fromkeys(v,0)
    # To count the vowels
    for char in s:
        if char in count:
            count[char] +=1
    return count

# def check_position(s,v):
# This will list the position of vowels in the word
# position = [i for i, char in enumerate(s) if char in v]

# print(position)

    
s = input('Enter a word:\n')
v = 'aeiou'

print('Via function define:')
check_string(s,v)
print(check_dictionary(s,v))

print('Via enumerate method:')

for position, char in enumerate(s):
    if char in v:
        print([char, position])
        







