# Enter a number and prints all the divisors

x = eval(input('Enter a number:'))


for i in range(1,x+1):
    if x%i == 0:
        print(i)
