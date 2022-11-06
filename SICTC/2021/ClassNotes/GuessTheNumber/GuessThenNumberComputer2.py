import random

print("Computer will now attempt to guess the number you input the quickest it can.")
secretNumber = input("Put a number from 0 - 100! >>> ")
# if user didn't input number, loop until they do
while secretNumber.isdigit() == False:
    secretNumber = input("Put a number from 0 - 100! >>> ")
# set secret number to int
secretNumber = int(secretNumber)
# default values
attempts = 0
lowest = 0
highest = 100
lied = False
guess = random.randint(lowest, highest)
# while guess is incorrect, keep looping.
while secretNumber != guess:
    print(f"Guessed {guess} which was incorrect, this is my {attempts} attempt.")
    # asks user if it was too high or low
    highOrLow = input("Was it too high or low? (h,l) >>> ").lower()
    # makes sure user inputs h or l
    while not highOrLow == "h" and not highOrLow == "l":
        highOrLow = input("Was it too high or low? (h,l) >>> ").lower()
    if highOrLow == "l":
        # number is too low
        if lowest < guess:
            # set range to include new lowest
            lowest = guess
    else:
        # number is too high
        if highest > guess:
            # set range to include new highest
            highest = guess
    # checks if user is lying
    if lowest+1 == highest-1 or lowest == highest:
        print("You lied to me!")
        lied = True
        guess = secretNumber
    # guess new number with new ranges
    if lied == False:
        guess = random.randint(lowest+1, highest-1)
        # add to attempts
        attempts += 1
# guess was correct
if lied == True:
    print("Cheater...")
else:
    print(f"Got it! Your number was {guess} and I got it in {attempts} attempts.")