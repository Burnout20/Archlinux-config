
import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
     players = input('How many players ')
     if players.isdigit():
         players = int(players)
         if 2<= players <=4:
             break
         else:
             print(' To much players ')
     else:
        print(' Invalid Input')

max_score = 24
player_score = [0 for _ in range(players)]


print(player_score)


        


















