# x = 25*x_q + 10*x_d + 5*x_n + 1*x_p

q = 25 # 1 quarter = 25 cents
d = 10
n = 5
p = 1

x = eval(input('Enter an mount no more than 1$ (in cents, i.e: 1 dollar = 100 cents):'))

x_q = x//q
x_d = (x - x_q*25)//d
x_n = (x - x_q*25 - x_d*10)//5
x_p = (x - x_q*25 - x_d*10 - x_n*5)//1


print(x_q, 'quarters')
print(x_d, 'dimes')
print(x_n, 'nickles')
print(x_p, 'pennies')

