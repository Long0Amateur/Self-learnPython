# Two dices roll program

# Visit:https://stackoverflow.com/questions/23598952/
# rolling-two-dice-and-tabulating-outcomes

import random

roll_time = int(input('How many times do you want to roll your dice?'))

roll = {}
# Note:
# {}: The two hash table types - dictionaries and sets
# []: Used to define mutable data types - lists, list comprehensions and for indexing/lookup/slicing.
# (): Define tuples, order of operations, generator expressions, function calls and other syntax.

for i in range(2,13):
    roll[i] = 0

double_roll = 0 # There will be chances that two dices roll the same number


for i in range(roll_time):
    first_dice = random.randint(1,6) # The first dice randomly rolls 1st to 6th side
    second_dice = random.randint(1,6)
    if first_dice == second_dice:
        double_roll +=1
    roll[first_dice+second_dice] +=1

for i in roll:
    print('%d - %d - %.2f%%' %(i, roll[i], float(roll[i])/float(roll_time)*100))  

print('Doubles - %d - %.4f%%' %(double_roll, float(double_roll)/float(roll_time)))
