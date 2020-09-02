# Temperature converter, C or F


x = eval (input('Enter a temperature:'))
y = eval(input('What unit is the temperature in, Celsius or Fahrenheit, enter as 1 for Celcius or 2 for Fahrenheit:'))


if y == 1:
    print(x, 'degrees Celcius equals', round((9/5)*x+32,2), 'degrees Fahrenheit')
else:
    print (x, 'degrees Fahrenheit equals', round((5/9)*(x-32),2), 'degrees Celcius')
