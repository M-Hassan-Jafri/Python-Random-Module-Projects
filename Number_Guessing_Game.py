import random as rd

print("\n\t\t\t\t\t\t\t\t<********* WELCOME TO NUMBER GUESSING GAME *********>")

score = 0

for i in range(5):

    num = int(input("\nYou can guess the number maximum 5 times.\nGuess the number from the range (1-10): "))
    random_number = rd.choice(range(1, 11))

    if num == random_number:
        score = score + 1
        print(f"\nYou guessed the right number!   \t\t\t\t\t\t Your score: {score}")

    else:
        print(f"\nYou failed to guess the right number!!! \t\t\t\t Your score: {score}")

print("\nYour final score: ", score)
