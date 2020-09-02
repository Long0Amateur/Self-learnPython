# A program counts how many squares from 1^2 to 100^2 end in a 4

count = 0

print(' A program counts how many squares from 1^2 to 100^2 end in a 4')

for i in range(1,101):
    if (i**2)%10==4:
        count = count + 1
        
print(count)
