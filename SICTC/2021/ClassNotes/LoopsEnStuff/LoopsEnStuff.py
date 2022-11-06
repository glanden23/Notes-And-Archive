import random
#while something is true:
#   do something

#while (boolean expression == True):
#   do 
#   this
#   algorithim

#iterable variable - a variable we add some value to
"""
i = 0
while i <= 1000:
    i+=1
    print(i)
"""
#print through array
"""
helloworld=["hello", "world"]
for x in helloworld:
    print(x)
"""
#guess number input
"""
g = int(input("Input a number 0-1000. >>> "))
guess = 0
while g != guess:
    guess = random.randint(0, 1000)
    print(guess)
"""
#print to 10,000 by 20.
"""
i = 10000
while i >= 1000:
    print(i)
    i-=20
"""
"""
test = []
dontstop = True
test.append(str(random.randint(0, 500)))
timesran = 0
while dontstop:
    test.append(test*9999999999)
    timesran+=1
    print(timesran)
    #print(test)
"""
"""
ui = input("Guess what? >>> ")
while(ui.lower() != "what" and ui.lower() != "wat" and ui.lower() != "wut" and ui.lower() != "watt" and ui.lower() != "wot"):
    ui = input("Guess what? >>> ")
print("Chicken butt.")
"""
"""
correctAnswers=["yes","no","y","n"]
ui = input("Would you like an apple pie with that? (y, n) >>> ")
while(not(ui in correctAnswers)):
    ui = input("Would you like an apple pie with that? (y, n) >>> ")
print("Ding fries are done!")
"""
# Loop until the user types in stop
#   allow for the user to type in numbers
#print out the total of those numbers.
"""
ui = input("How much do you want? >>> ")
total = 0
while(ui != "stop"):
    total+=int(ui)
    print(total)
    ui = input("Would you like some more? (\"stop\" to quit) >>> ")
"""
# List version
"""
total = []
ui = input("Give me a number.")
while(ui != "stop"):
    total.append(float(ui))
    print(f"{sum(total)} with a total of {len(total)} entiries.")
    ui = input("Give me a number.")
print(sum(total))
"""
#Program takes in user input of numbers until the user enters the number 0, tell the user how many even numbers they entered.
"""
number = int(input("Enter a number. >>> "))
totalEvens = 0
while(number != 0):
    if (number%2 == 0):
        totalEvens+= 1
    number = int(input("Enter a number. (0 to stop) >>> "))
print(f"Got {totaleven} even numbers.")
"""
