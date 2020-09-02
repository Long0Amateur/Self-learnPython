# A program finds all 4 of the perfect numbers that are less than 10000
# A perfect number is equal to sum of all of its divisors


for x in range(1,10000+1):
    s = 0
    for i in range(1,x):
        if x%i == 0:
            s = s + i
         
    if x == s:
        print(x)
        
