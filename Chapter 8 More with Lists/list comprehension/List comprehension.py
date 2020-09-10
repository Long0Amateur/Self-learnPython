# List comprehension

string = 'Hello'

L = [1,14,5,9,12]
I = L[:] # copy
M = ['one','two','three','four','five','six']
T = M[:]
O = M[:]

N = [i for i in range(5)]
print(N)        # print [0,1,2,3,4]

P = [0 for i in range(10)]
print(P)        # print [0,0,0,0,0,0,0,0,0,0]

L =[i*10 for i in L]
print(L)        # print [10,140,50,90,120]

string = [c*2 for c in string]
print(string)   # print ['HH','ee','ll','ll','oo']

M = [m[0] for m in M]
print(M)        # print ['o','t','t','f','f','s']

I = [i for i in I if i<10]
print(I)        # print [1,5,9]

T = [m[0] for m in T if len(m) == 3]
print(T)        # print ['o','t','s']
                # print the first element of characters which have length equals 3
                # m[0] + m[1] + m[2] => print all elements of characters which have length equals 3

H =[]
for i in O:
    if len(i) == 3:
        H.append(i)
print(H)        # print ['one', 'two','six']
