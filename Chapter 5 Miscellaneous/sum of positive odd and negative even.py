# A program to compute the sum 1-2+3-4+...+1999-2000

s = 0
s1= 0
for i in range(1,2001):
    if i%2 == 0:#even
        s = s + i*(-1)
        
    if i%2 == 1:#odd
        s1 = s1 + i

print(s+s1)

