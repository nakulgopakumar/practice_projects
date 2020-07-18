import random


#function to roll the dice and return a number
def roll_dice():
    num=random.randint(1,6)
    return num

print("Starting the game....\n You and computer both have 100$ in hand.")
print("You can increase the bet amount for every roll after this....\n\n")
print("....\n Call your dice..  (any number betweeen 1 and 6) ")
choice = int(input())
print("\nRolling....")
rolled = roll_dice()
print("You rolled .......:   " + str(rolled))

if choice == rolled:
    print("You won")
else:
    print("You lost")

