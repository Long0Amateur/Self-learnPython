# A program picks a random ordering of players in a game

from random import shuffle

players = ['Joe','Bob','Sue','Sally']
shuffle(players)

for p in players:
    print(p,'- It is your turn.')
