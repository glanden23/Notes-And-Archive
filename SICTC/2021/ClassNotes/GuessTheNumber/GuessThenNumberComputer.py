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
guess = random.randint(0, 100)
# while guess is incorrect, keep looping.
while secretNumber != guess:
    print(f"Guessed {guess} which was incorrect, this is my {attempts} attempt.")
    # guess new number with new ranges
    guess = random.randint(0, 100)
    # add to attempts
    attempts += 1
# guess was correct
print(f"Got it! Your number was {guess} and I got it in {attempts} attempts.")