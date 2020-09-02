# https://stackoverflow.com/questions/48403767/merge-two-strings-with-alternate-chars-as-output
s1 = input('Enter the first string:')
s2 = input('Enter the second string:')

if len(s1) != len(s2):
    print('Not the same length')
else:
    # String concatenation

    s = ''
    for i in range(len(s1)):
        s += s1[i] + s2[i]
    print(s)

    print('Via enumerate method:')
    result = ''
    for i,c in enumerate(s1):
        result += c + s2[i]

    print(result)
        

    


    
