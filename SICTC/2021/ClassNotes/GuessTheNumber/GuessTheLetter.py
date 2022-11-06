import random
import string

strikes = 0
secretLetter = random.randint(0, len(string.ascii_lowercase))
ui = input("Input a letter to guess. >>> ")
while not ui.isascii():
    ui = input("Input a letter to guess. >>> ")
ui = string.ascii_lowercase.index(ui.lower())
while ui != secretLetter:
    strikes+=1
    if ui < secretLetter:
        print(f"Too low! {strikes}/3 before failing!")
    else:
        print(f"Too low! {strikes}/3 before failing!")
    if strikes == 3:
        ui = secretLetter
    else:
        ui = input("Input a letter to guess. >>> ")
        while not ui.isascii():
            ui = input("Input a letter to guess. >>> ")
        ui = string.ascii_lowercase.index(ui.lower())
if strikes == 3:
    print("You failed! Ran out of strikes.")
else:
    print("You got it! Congrats!")