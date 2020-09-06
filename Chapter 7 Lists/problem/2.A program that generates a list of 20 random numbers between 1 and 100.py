# A program that generates a list of 20 random numbers between 1 and 100

from random import randint

L=[]
for i in range(20):
    L.append(randint(1,100))

# Print the list
print(L,'\n')

# Print the average of the elements in the list
avg = sum(L)/len(L)
print('The average of the elements in the list:',round(avg,2))

# Print the largest and smallest values in the list

L.sort()

print('The largest value:',L[-1])
print('The smallest value:',L[0])

# Print the second largest and smallest values in the list

print('The second largest:',L[-2])
print('The second smallest:',L[1])

# Print how many even/odd numbers are in the list

even_count = 0

for num in L:
    if num%2 == 0:
        even_count+=1
         
print('There are',even_count,'even numbers in the list.')
print('There are',len(L)-even_count,'even numbers in the list.')

# Print the even/odd numbers in the list

M = [x for x in L if x%2 == 0]
N = [y for y in L if y%2 != 0]

print('The even numbers:',M)
print('The odd numbers:',N)
