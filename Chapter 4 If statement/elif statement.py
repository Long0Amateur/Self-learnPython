# elif statement

grade = eval(input('Enter your score:'))
if grade>=90:
    print('A')
elif grade>=80: # if grade >= 80 and grade < 90: print('B')
    print('B')
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
else:
    print('F')
    
