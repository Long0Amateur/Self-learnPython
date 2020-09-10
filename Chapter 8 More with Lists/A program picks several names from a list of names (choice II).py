# A program picks several names from a list of names

from random import sample

names = ['Joe','Bob','Sue','Sally']

team = sample(names,2) # Picks 2 names from the list

print(team)
