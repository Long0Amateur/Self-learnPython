
print('Hello pattern if rand_num is placed outside for statement')
from random import randint

rand_num = randint(5,25)
for i in range(rand_num):
    print('Hello')

print(sep='')
print('Hello pattern if rand_num is placed inside for statement')

for i in range(6):
    rand_num = randint(1,5)
    print('Hello'*rand_num)
