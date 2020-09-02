# A program asks user to enter 5 letters and prints specific letters only

s = ''
for i in range(5):
    t = input('Enter a letter:')
    
    if t in 'aeiou':
        # if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u':
        s = s + t

print(s)



    
