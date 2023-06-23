import random as rnd

print("\n******** WELCOME TO DICE SIMULATOR *********\n")

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

response = input("Do you want to roll the dices.? (y/n) ")

r = True

while r == True or r.lower() == 'y':

    if response.lower() == 'y':
        outcome1 = rnd.choice(dice1)
        outcome2 = rnd.choice(dice2)

        if outcome1 == 6 and outcome2 == 6:
            print("Congratulations! you got double 6. You are lucky.\n")
        else:
            print("You got:", outcome1, "and", outcome2, "\n")

    else:
        print("Fun playing Dice Simulator? Hope you'll come to play again. Until then goodbye!!")

    r = input("Did you want to play again..?? (y/n) ")