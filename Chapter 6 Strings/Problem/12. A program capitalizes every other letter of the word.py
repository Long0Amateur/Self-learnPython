# A program capitalizes every other letter of the word
#      rhinoceros
#      rHiNoCeRoS
#index 0123456789

# Visit https://stackoverflow.com/questions/50049309/alternating-letter-in-python

def odd_upper(word):
    result = ''
    
    for index, letter in enumerate(word): 
    # the odd will be upper
        if index % 2 != 0:
            result += letter.upper()
        else:
            result += letter.lower()
        
    return(result)

# Drive code

s = input('Enter a word:')

print(odd_upper(s))




