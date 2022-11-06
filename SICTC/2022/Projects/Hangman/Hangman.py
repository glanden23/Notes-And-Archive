from random import randint


def begin():
    clearScreen()                                                   # Calls clearScreen function which clears the terminal.
    word = list(pickWord().replace("\n", ""))                       # Grabs from word list, removes formatting and makes it a list for comparing.
    guess = []                                                      # Creates an empty list
    guessed = ""                                                    # Creates currently guessed letters string for adding to later.
    for _ in word:                                                  # Puts blanks into empty guess list for formatting.
        guess.append("")
    guessa = 0                                                      # Creates guess attempts
    while guess != word:                                            # Loops until word matches the guess
        hangmanArt(guessa, guess, guessed, word)                    # Calls function to return art and formatting. (wouldn't put in function normally but its super big and messy)
        print(f"Currently {6-guessa}/6 attempts remaining.")        # Prints out the remaining attempts.
        ui = input("Guess a letter >>> ").lower()                   # Asks for letter and lowercases it.
        while len(ui) > 1 or not ui.isalpha():                      # Loops until ui is only one letter and not a number
            ui = input("Guess a letter >>> ").lower()               # Asks for letter and lowercases it.
        if ui not in guessed:                                       # If the UI is not in guessed, it will add it to the failed guesses string 
            guessed+= ui+" "
        if ui in word:                                             # Loops through the word and finds what letter matches in the word and then adds it to the correct guess list.
            for i in range(len(word)):
                if word[i] == ui:
                    guess[i] = ui
        else:
            guessa+=1                                               # adds 1 to the attempt
        clearScreen()                                               # Calls clearScreen function which clears the terminal.
    print(f'You got it! The word was {"".join(word)}.')             # Once loop breaks, calls print statement to say the user has won.
        

def clearScreen():
    print("\n"*500)                                                 # Prints new lines to remove extra text from terminal.

def pickWord():                                                     # Opens the words file and grabs a random word. (Provided by: http://www.mieliestronk.com/corncob_lowercase.txt)
    file = open("./words.txt", "r")
    wordList = file.readlines()
    return wordList[randint(0, len(wordList))]
    
def hangmanArt(aWrong, guess, guessed, word):                       # Prints hangman art and formats the general game layout. (guesses, blank spaces, etc...)
    if (aWrong == 6):
        print(f"You failed... The word was {''.join(word)}")
        print("""
 O
-|-
/\\
              """)
        exit()
    elif(aWrong == 5):
        print("""
 O
-|-
/
              """)
    elif(aWrong == 4):
        print("""
 O
-|-
              """)
    elif(aWrong == 3):
        print("""
 O
-|
              """)
    elif(aWrong == 2):
        print("""
 O
-
              """)
    elif(aWrong == 1):
        print("""
 O
              """)
    formatted = ""
    for i in guess:                                                  # Loops through guess list and adds a "_ " for every empty value inside it. 
        if i == "":                                                  # This is than added to the formatted string which is printed out in the end.
            formatted+="_ "
        else:
            formatted+=i
    print(formatted)
    if guessed != "":                                                # Checks to make sure guessed list isn't empty and prints out the failed attempts if not.
        print(f'{guessed}')
            
    

if __name__ == "__main__":
    begin()