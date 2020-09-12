# A program asks user to enter a list of strings, creates a new list
# that consists of those strings with their first charactewr removed
# i.e L = [123,456]
# Remove the first character
#     L = [23,56]

L  = input('Enter a list of string:').split()
 
for i in range(len(L)):
    L[i] = L[i][1:]

print(L)
