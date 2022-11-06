import random

computerGuess = True
#Build out a program that asks the user to guess a number.
#   (just like our app...)
if computerGuess == False:
    secretNumber = 55
    strike = 3
    ui = input("Guess a number from 0 - 100! >>> ")
    # if ui is not a digit, don't move on.
    while ui.isdigit() == False:
        ui = input("Guess a number from 0 - 100! >>> ")
    # set ui to an int.
    ui = int(ui)
    # loop until user guesses number
    while ui != secretNumber:
        strike -= 1
        if ui < secretNumber:
            print(f"Incorrect, too low! You have {strike} attempts remaining...")
        else:
            print(f"Incorrect, too high! You have {strike} attempts remaining...")
        if strike == 0:
            ui = secretNumber
        else:
            ui = input("Guess a number from 0 - 100! >>> ")
            # if ui is not a digit, don't move on.
            while ui.isdigit() == False:
                ui = input("Guess a number from 0 - 100! >>> ")
            # set ui to an int.
            ui = int(ui)
    if strike == 0:
        print("You ran out of tries.")
    else:
        print("You got it!")

if computerGuess == True:
    print("Computer will now attempt to guess the number you input the quickest it can.")
    secretNumber = input("Put a number from 0 - 100,000,000! >>> ")
    # if user didn't input number, loop until they do
    while secretNumber.isdigit() == False:
        secretNumber = input("Put a number from 0 - 100,000,000! >>> ")
    # set secret number to int
    secretNumber = int(secretNumber)
    # default values
    lowest = 0
    highest = 100000000
    attempts = 0
    guess = random.randint(lowest, highest)
    # while guess is incorrect, keep looping.
    while secretNumber != guess:
        if secretNumber > guess:
            # number is too low
            if lowest < guess:
                # set range to include new lowest
                lowest = guess
        else:
            # number is too high
            if highest > guess:
                # set range to include new highest
                highest = guess
        print(f"Guessed {guess} which was incorrect, this is my {attempts} attempt. Range: {lowest}-{highest}")
        # guess new number with new ranges
        guess = random.randint(lowest+1, highest-1)
        # add to attempts
        attempts += 1
    # guess was correct
    print(f"Got it! Your number was {guess} and I got it in {attempts} attempts. Final Range: {lowest}-{highest}")