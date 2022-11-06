'''
range(10)
#generate a list of numbers from 0 to 10.
print(range(10))
print(range(0, 10, 2))
print(range(0, 100))

#for i many times in range(number of times, I need it to run, step by)
for i in range(0, 11, 2):
    print(i)

#print out odd numbers from 37 to 83
for i in range(37, 84, 2):
    print(i)

#for someVariable in a list:
#   do something
for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)

name=["bob","ryan", "will", "wyatt", "sydni", "aidan", "paige"]
for i in name:
    #every interation -> i becomes that item in the list
    print(i)
'''

"""
number=[7,60,5,24,9,20,12,22,21,10]
for i in range(len(number)):
    print(f"First Value: {number[i]}")
    number[i]*=2
    print(f"Second Value: {number[i]}")
print(number)

for i in number:
    index = number.index(i)
    number[index] = i * 2
    print(number[index])
print(number)

for i in number:
    i*=2
    print(i)
"""

#alogirthm that takes in user input
#   ask the user for 10 numbers
#   print out the total of those numbers
"""
print("Give me 10 numbers! >>> ")
total = 0
for i in range(10):
    ui = float(input(">>> "))
    total+=ui
print(total)
"""

"""
#Example of where while statement would be better.
for i in range(999999999999999999999):
    ui = input("Guess what? >>> ")
    if ui.lower() == "what":
        print("Chicken Butt")
        break
"""
#name="jimbob"
"""
for i in name:
    print(i) # i is the letter
for i in range(len(name)):
    print(name[i]) # i is the index
"""
name = "spongebob squarepants"
vowels = 0
vowelList = ["a", "e", "i", "o", "u"]
for i in name:
    if i in vowelList:
        vowels+=1
print(vowels)