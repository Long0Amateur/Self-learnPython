# A program asks user for an integer and creates a list that consists
# of the factors of that integer

x = eval(input('Enter an integer:'))

M = []

for i in range(1,x+1):
    if x%i == 0:
        M.append(i)

print('The factors of',x,':',M)
