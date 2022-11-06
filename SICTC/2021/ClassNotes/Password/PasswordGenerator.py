import random
import string

upperCase = list(string.ascii_uppercase)
lowerCase = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

def generate(numberUpper, numberLower, num, sym):
    password = ""
    for i in range(numberUpper):
        password+=upperCase[random.randint(0, len(upperCase)-1)]
    for i in range(numberLower):
        password+=lowerCase[random.randint(0, len(lowerCase)-1)]
    for i in range(num):
        password+=numbers[random.randint(0, len(numbers)-1)]
    for i in range(sym):
        password+=symbols[random.randint(0, len(symbols)-1)]
    #https://stackoverflow.com/questions/2668312/shuffle-string-in-python
    password = list(password)
    random.shuffle(password)
    return "".join(password)

UI = input("Would you like to make a new password? (quit to cancel) >>> ")
while UI != "quit":
    numberUpper = int(input("How many upper? >>> "))
    numberLower = int(input("How many lower? >>> "))
    num = int(input("How many numbers? >>> "))
    sym = int(input("How many symbols? >>> "))
    print(generate(numberUpper, numberLower, num, sym))
    UI = input("Would you like to make a new password? (quit to cancel) >>> ")
print("Goodbye.")