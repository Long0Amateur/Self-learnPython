
# Fibonacci sequence

x = eval(input('How many Fibonacci numbers to print?'))
y = 1
z = 0

for i in range(x):
    y = y+z
    z = y-z
    print(i,'---',y,'---',z)
