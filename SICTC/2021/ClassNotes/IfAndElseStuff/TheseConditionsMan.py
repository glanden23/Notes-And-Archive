#conditionals are based on boolean statements
print(type(5))
print(type("true"))
print(type(True))
# True and False are built into Python
# Converting Functions
#int()
#str()
#float()
#bin()
#bool()

print(bool(1))
print(bool(0))
print(bool(10))

#if something is true:
#   then do this
#else if something else is true:
#   tehn do that
#all else fails:
#   then do this

x=4
if x == 4:
    print("correct")
elif x > 4:
    print("too high")
else:
    print("too low")

#ask the user if they had breakfast
#   if they did, ask them what they ate.

question = input("Did you eat breakfast?")
if question.lower() == "yes":
    print("What did you eat?")
elif question.lower() == "no":
    print("You should eat breakfast.")
else:
    print("Sorry, I don't understand that.")

'''
    Relational Operators
        == equal to
        <= less than or equal to
        >= greater than or equal to
        != not equal to
        not  opposite of the boolean
        and means both sides have to be true
        or means one side has to be true
'''

x=input('what is your x value')
y=input("what is your y value")

if x>=0 and y>=0 and x<=50 and x>=50:
    print("You're in the box!")
else:
    print("You went outside the box!")