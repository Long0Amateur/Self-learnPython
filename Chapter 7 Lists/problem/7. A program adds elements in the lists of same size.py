# A program adds elements in the lists of the same size

L = [3,1,4]

M = [1,5,9]

if len(L) == len(M):
    N = [L[i]+M[i] for i in range(len(L))]
    print(N)

else:
    print('The lists are not the same length.')


