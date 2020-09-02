# A program asks user to enter a number and
# prints the sum of the divisors of number

x = eval(input('Enter a number:'))

s = 0
for i in range (1,x):
    if x%i == 0:
        s = s + i
        print(i)
print('The sum of divisors of',x,'is',s)
