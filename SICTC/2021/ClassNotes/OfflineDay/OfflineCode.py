import random
#print("Hello World")
#ui = input("What is your name? >>> ")
#print(f"Hello {ui}!")

def userLogin():
    username = input("What is your username? >>> ")
    masterusername = "HelloWorld"
    masterpassword = "World"
    if not("@" in username) and not("." in username):
        if masterusername == username:
            print("Hello World! Nice to see you here. Please enter your password before we continue.")
            password = input("Please enter your password! >>> ")
            if masterpassword == password:
                print("Welcome Hello World. Glad to see it is really you. Hope you are doing well.")
                print("Lets play a game, shall we?")
                print("Pick a number and I'll guess it.")
                print("Or would you like for me to play agaisnt myself?")
                ui = input("Against or Self? >>> ")
                if ui.lower() == "against":
                    guessNumberPlayer()
                else:
                    guessSelf()
            else:
                print("You seem to have gotten your password incorrect. Please check again.")
                userLogin()
        else:
            print("You seem to not remember who you are? Are you sure you are in the right place?")
            userLogin()
    else:
        print("Invalid username!")

def guessSelf():
    number = random.randint(0, 10000)
    print(f"Starting new game. Don't tell myself this but the number is {number}")
    numberGuess = random.randint(0, 10000)
    timesGuessed = 1
    while number != numberGuess:
        timesGuessed = timesGuessed + 1
        numberGuess = random.randint(0, 10000)
        if number == numberGuess:
            print(f"Got it! The number was {number} and it took me {timesGuessed} attempts to guess it.")
            ui = input("Would you like for me to play again? >>> ")
            if ui.lower() == "yes" or ui.lower() == "y":
                guessSelf()
            else:
                print("Okay... signing you out now. Thanks for playing!")
                userLogin()
        else:
            print(f"Guessed {numberGuess} but the actual number was {number}. This is attempt {timesGuessed}!")

def guessNumberPlayer():
    number = float(input("Number? >>> "))
    if number > 1000:
        print("Your number is too big! Please input a number less than 1000.")
        guessNumberPlayer()
        return
    numberGuess = random.randint(0, 1000)
    timesGuessed = 1
    while number != numberGuess:
        timesGuessed = timesGuessed + 1
        numberGuess = random.randint(0, 1000)
        if numberGuess == number:
            print(f"Got it! Your number was {number}? This took me {timesGuessed} times.")
            ui = input("Would you like to play again? >>> ")
            if ui.lower() == "yes" or ui.lower() == "y":
                guessNumberPlayer()
            else:
                print("Okay... signing you out now. Thanks for playing!")
                userLogin()
        else:
            print(f"Guessed {numberGuess} but that was incorrect! I've guessed {timesGuessed} numbers so far!")


if __name__ == "__main__":
    userLogin()