# A prograns asks user for an integer and tell them if it is squarefree or not
# A squarefree is an integer indivisble by any perfect squares other than 1
# 9 is perfect square
# Square frees: 1,2,3,5,6,7,10,11,13,14,15,17,19
# Exp: 42 is squarefree because its divisors are 1,2,3,6,7,21,and 42,
# and none of those numbers (except 1) is a perfect square

        
# check perfect square

x = eval(input('Enter an integer:'))

x_square = x**2

if (x_square**2) == x:
    print(x,'is perfect square')

else:
    print(x,'is not perfect square')

# check square free

y = eval(input('Enter an integer:'))

for i in range(2,y
# check divisors
if y%x_square == 1:
    print(y,'is square free')

else:
    print(y,'is not square free')

        
   
