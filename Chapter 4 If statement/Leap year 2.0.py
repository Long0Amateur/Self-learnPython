# Leap year

x = eval(input('Enter a year:'))

if (x%4) == 0:
    if(x%100) ==0:
        if (x%400) == 0:
            print(x,'Leap year')
        else:
            print(x,'Not leap year')
    else:
        print(x,'Leap year')

else:
    print(x,'Not leap year')
