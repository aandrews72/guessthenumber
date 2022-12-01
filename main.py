#Generate number between 0-100
import random 
number = random.randint(1,99)
win = False
while win == False:
#Ask user for a guess via input
    guess = int(input("Guess a number between 0 and 100: "))
    if guess == number:
        print("You won!")
        win == True
        break
    else:
#Compare user guess to number and ask again or congratulate the user using loops
        if guess > number:
            print("Too high.")
        else:
            print("Too low.")