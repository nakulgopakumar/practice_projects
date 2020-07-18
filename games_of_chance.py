import random
bet_amount = [100, 100]


#function to update bet amount of user and computer
def bet ():
    print("Enter the amount you want to bet......\n")
    bet_by_user = int(input())
    bet_by_computer = computer_bet()
    print("\nThe computer has bet....." + str(bet_by_computer))
    bet_amount[0] = bet_amount[0]-bet_by_user
    bet_amount[1] = bet_amount[1]-bet_by_computer
    return bet_by_user,bet_by_computer
    
#function to determine winner and winnings
def winner_decider(choice,rolled,bet_by_user,bet_by_computer):
    if choice == rolled:
        print("You won this round")
        bet_amount[0] = bet_amount[0]+bet_by_user+bet_by_computer
    else:
        print("You lost this round")
        bet_amount[1] = bet_amount[1]+bet_by_computer+bet_by_user

#computer bet generator
def computer_bet():
    num=random.randint(1,100)
    return num

#function to handle betting money

        
#function to roll the dice and return a number
def roll_dice():
    num=random.randint(1,6)
    return num

game = 1
while game == 1:
#starting game and updating bets
    print("Starting the game....\n You and computer both have 100$ in hand.")
    bet_u,bet_c = bet()

    #rolling dice
    print("....\n Call your dice..  (any number betweeen 1 and 6) ")
    choice = int(input())
    print("\nRolling....")
    rolled = roll_dice()
    print("You rolled .......:   " + str(rolled))

    #determining winner
    winner_decider(choice,rolled,bet_u,bet_c)

    #current winnings
    print("Your money : " + str(bet_amount[0]) + "$")
    print("Computer's money : " + str(bet_amount[1]) + "$")

    print("\n\n Press 1 to continue. Press 2 to exit")
    game = int(input())
    if game == 2:
        break
    
