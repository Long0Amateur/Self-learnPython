# A program rotates the elements in the list
# i.e the element at first index moves to the second index,
# the element at second index moves to the third index, etc.
# the element at last index moves to the first index



def rotate(L,n):
    return L[n:] + L[:n]

L=[1,2,3,4,5,6]


for i in range(len(L)):
    print(rotate(L,i))
