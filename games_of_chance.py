import random

#function to roll the dice and return a number
def roll_dice():
    num=random.randint(1,6)
    return num

choice = roll_dice()
print("You rolled .......:   " + str(choice))

