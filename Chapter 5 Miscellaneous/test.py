alist = [-45,0,3,10,90,5,-2,4,18,45,100,1,-266,706]
largest = 0
second_largest = 0
for large in alist:
  if second_largest < large:
    second_largest = large

  if largest < large:
    temp = second_largest
    second_largest = largest
    largest = temp

print( "First Highest:",largest)
print ("Second Highest:",second_largest)
