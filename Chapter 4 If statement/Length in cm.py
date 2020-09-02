# A program that asks the user to enter a length in centimeters

x = eval(input('Enter a length in centimeters:'))
if x<0:
    print('Invalid entry!')
else:
    print(x, 'centimers equal',round(x/2.54,2),'inches')
    
