# A program asks user for a polynomial function and prints out its derivative

# Visit: https://stackoverflow.com/questions/58350036/
# how-to-make-python-reading-a-user-input-function-like-fx-2x23x1


from sympy import sympify, Symbol

x = Symbol('x')
y = sympify(input('Enter polynomial function [i.e 2x^2, input as 2*x**2]:\n'))

yprime = y.diff(x)
print('The derivate of',y,'is:\n',yprime)


# import sympy as sp

# x = sp.Symbol('x')
# y = input("Type a polynomial function:\n")

# newY = ' '
# for i in range(len(y)):
#    if y[i] == '^':
#        newY = newY + '**'
#    else:
#        newY = newY + y[i]
#    if i<len(y)-1:
#        if y[i].isdigit() and y[i + 1].isalpha():
#            newY = newY + '*'

# y = eval(newY)
# print(y.diff(x))

