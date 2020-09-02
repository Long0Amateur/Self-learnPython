# hollow asterisk box (19x4)

x = eval(input('How wide you want the box?'))
y = eval(input('How hide you want the box?'))
print('*'*x)
for i in range(y-2):
    print('*' + ' '*(x-2) + '*')
print('*'*x)
