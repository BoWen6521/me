"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random



def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("Welcome to the guessing game!")
    print("A number between _ and _ ?")
    
    while True:
        try:
            lowerBound = int(input("Enter an lower bound: "))
            break
        except Exception as e:
            print("Please enter integer only ({})".format(e))

    
    while True:
        try:
            upperBound = int(input("Enter an upper bound: "))
            break
        except Exception as e:
            print("Please enter integer only ({})".format(e))
    actualNumber = random.randint(lowerBound, upperBound)

    if upperBound < lowerBound:
        print('Upper bound greater than lower bound.')
        while True:
            try:
                upperBound = int(input("Enter an upper bound: "))
                break
            except Exception as e:
                print("Please enter integer only ({})".format(e))

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        while True:
            try:
                guessedNumber = int(input("Guess a number: "))
                break
            except Exception as e:
                print("Please enter integer only ({})".format(e))
                
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
        elif guessedNumber < actualNumber and lowerBound < guessedNumber < upperBound:
            print("Too small, try again :'(")
        elif guessedNumber > actualNumber and lowerBound < guessedNumber < upperBound:
            print("Too big, try again :'(")
        else:
            print("You are outside the bound, try again")
    return "You got it!"



if __name__ == "__main__":
    print(advancedGuessingGame())
