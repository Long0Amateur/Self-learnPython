# A progran to print out the pattern where it ends at the number the user enters
# 1
#  2
#   3
#    4

s = input('Enter a number:')
for i in range(s):
    print(s[:i])
    
