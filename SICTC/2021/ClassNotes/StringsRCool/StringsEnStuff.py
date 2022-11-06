print("String Manipulation")
'''
    Data Types:
        Int, FLoat, Strings, List, Booleans
        Primitive: Int, Booleans, Float
        Non-Primitive: Strings, List
'''

#String Math
#name="bobby"
#age=17
#print("Hello " + "bobby") # string addition
#print("Hello " + name)
#print("Your age is " + str(age))

#converts to int
#print(int("17"))

#converts an int or anything to a string
#print(str(age))

#name=input("your name ")
#grade=input("grade level ")
#print("Wow, "+name+" you're in the "+grade+" grade")

#pet=input("What is your pets name? ")
#age=input("How old is your pet? ")
#size=input("How big is your pet? ")
#smell=input("how does your pet smell? ")

#print("Your pet, "+pet+", sounds like a cool pet. I can't believe they are "+age+" and "+size+"!")
#print("I like "+smell+" smelling pets.")

"""output=(f'''
Your pet, {pet}, sounds like a cool pet.
I can't believe they are {age} and {size}
I like {smell} smelling pets''')"""
#print(output)

#convert your name to binary
#print(bin(72))

#convert a character to an int
#print(ord("B"))

#print(bin(ord("B"))

#print(bin(16))
#print(bin(-16))
#print(bin(0))

"""
gasCost=float(input("How much does gas cost? "))
gasTaken=float(input("How many gallons did you purchase? "))
gasCost=cost*gal
print(str(gasCost))

print("poop"+"poop")
print("poop"*20)"""

name=input("What is your name? ")
name=name.title()
prefix=input("What is your title (Mr, Mrs, Dr, Sir)").title()

print(f"Hello, {prefix}. {name}")