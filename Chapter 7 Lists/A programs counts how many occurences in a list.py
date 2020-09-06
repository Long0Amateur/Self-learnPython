# Given a list L contains numbers between 1 and 100
# A programs creates a new list whos first element is how many ones are in L,
# whose second element is how many twos are in L, etc


L = [1,2,3,3,1,4,1,2,4]
            
frequencies =[]
for i in L:
    frequencies.append(L.count(i))

print(L)
print('The occurences:\n',frequencies)
