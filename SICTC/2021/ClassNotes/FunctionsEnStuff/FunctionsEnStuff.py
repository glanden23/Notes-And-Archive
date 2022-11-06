'''
    Procedures - Purple Blocks
    Functions - Block of code that completes an algorithm
    Methods - Methods are used with objects and classes
'''

#define a function call howdy
def howdy():
    #print howdy
    print("howdy")

#call the print function
#print("the message to print")
#call the howdy function
#howdy()

def adding():
    a=int(input("Give me a number"))
    b=int(input("Give me a number"))
    print(a+b)

#define a function that adds 2 number together
#adding()

def ymxb(m, x, b):
    print(f"x: {x} | y: {m*x+b}")

def returnYMXB(m, x, b):
    return (m*x+b)

print("\tx   |   y")
print("\t---------")
for i in range(101):
    #place in the 3 arguments
    stri = str(i)
    if len(stri) == 1:
        stri = "00"+stri
    elif len(str(i)) == 2:
        stri = "0"+stri
    else:
        stri = stri
    print(f"\t{stri} | {returnYMXB(3,i,-2)}") #i is the x value for this equation
print("\t---------")