# A progran to print out the pattern where it ends at the number the user enters
# 1
#  2
#   3
#    4

n = eval(input('Enter a number:'))


# Convert the integer input to a list L =[1,2..n]
L =[]
for i in range(0,n):
    L.append(i+1)

# Convert list to string
N = ''.join([str(num) for num in L])

for index, number in enumerate(N):
    print(' '*index + number)
