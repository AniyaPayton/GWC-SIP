from random import *

aRandomNmber = randint (1,20)
guessNumber = 0


while guessNumber < 3:
    guess = input ("Guess a number between 1-20 (inclusive):")

    if (guess) == aRandomNmber:
        print("You got it")
        break
    else
        print("Your guess is too high")
                guessNumber += 1
    elif (guess) < aRandomNmber:
        print("Your guess is to low")
        guessNumber += 1
