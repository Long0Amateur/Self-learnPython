# A program asks user to enter a list of integers

# Visit:
# https://thispointer.com/
# python-get-number-of-elements-in-a-list-lists-of-lists-or-nested-list/

from random import randint
L=[]
for i in range(10):
    L.append(randint(1,10))

print(L,'\n')

# Print the total number of items in the list
print('The total number of items in the list:',len(L),'\n')

# Print the last item in the list
print('The last number in the list:',L[-1],'\n')

# Print the list in reverse order
M = L[:]
L.reverse()
print('The list in reverse order:',L,'\n')

# Print Yes if the list contains a 5 and No otherwise
# Print the number of fives in the list as well

if 5 in L:
    print('Yes. The list contains',L.count(5),'five.','\n')
    
else:
    print('No. The list does not contain 5.\n')

# Remove the first and last items from the list, sort the remaining item, and print the result
del M[0]
del M[-1]
M.sort()
print('The first and last numbers from the list are removed. The sorted result:\n',M,'\n')

# Print how many integers in the list are less than 5

count = 0
for i in M:
    if i < 5:
        count+=1
print('Integers less than 5:',count)
print('Integers more than 5:',len(M)-count)

    

