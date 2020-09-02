# Python program to check if year is a leap year or not

x = eval(input('Enter a year:'))


for i in range(1600,x+1):
    if (i%4) == 0:
        if (i%100) == 0:
            if (i%400) == 0:
                print(i, 'Leap year')
            else:
                print(i,'Not leap year')
        else:
            print(i,'Leap year')
    else:
        print(i, 'Not leap year')

   
        
