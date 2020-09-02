# flag, prime numbers

x = eval(input('Enter number:'))

flag = 0
for i in range (2,x):
    if x%i == 0:
        flag = 1

if flag == 1:
    print(x,'is not prime')

else:
    print (x,'is prime')
