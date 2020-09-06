# A program modifies the list [8,9,10] and prints the final result as
# [4,5,6,25,10,17,4,5,6,10,17]

L =[8,9,10]

# Set the second entry (index 1) to 17
L[1] = 17

# Add 4,5, and 6 to the end of the list
L.append(4)
L.append(5)
L.append(6)

# Remove the first entry from the list
del L[0]

# Sort the list
L.sort()

# Double the list
N=L+L

# Insert 25 at index 3
N.insert(3,25)

print(N)



