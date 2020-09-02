# Enter a word: buffalo
# buffa
# lo


s = input('Enter a word:')
c = input('Which letter to slice:')


# This will print out the first part before 'a'
print(s[:s.index(c)+1]) 

# This will print out the second part after 'a'
print(s[s.index(c)+1:]) 
    


