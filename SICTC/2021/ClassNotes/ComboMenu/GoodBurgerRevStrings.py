#Iteration 1
total=0
orderInformation = "\nYour Order:\n"
chooseSandwich,chooseFries,chooseDrink = False,False,False

sandwich = input("Would you like a sandwich? (y,n) >>> ")
if sandwich == "y":
     print("Chicken ($5.25), Beef ($6.25), Tofu ($5.75)")
     sandwich = input("Which sandwich would you like? (c,b,t) >>> ")
     if sandwich=="c" or sandwich=="b" or sandwich=="t":
          orderInformation += f"\tSandwich:\t{sandwich}\n"
          chooseSandwich = True
     if sandwich == "c":
          total += 5.25
     elif sandwich == "b":
          total += 6.25
     elif sandwich == "t":
          total += 5.75

#Iteration 2
drink = input("Would you like a drink? (y,n) >>> ")
if drink == "y":
     chooseDrink= True
     drink = input("Which size? (s,m,l) >>> ")
     if drink == "s":
          total += 1
     elif drink == "m":
          total += 1.75
     elif drink == "l":
          #ask if they want a child size for $0.38 more
          drink = input("Would you like a child size for $.38 more? (y,n) >>> ")
          if drink=="y":
               total += 2.25+.38
          else:
               total += 2.25
     orderInformation+=(f"\tDrink:\t\t{drink}\n")
     

#Iteration 3
fries = input("Would you like fries with that? (y,n) >>> ")
if fries == "y":
     chooseFries=True
     fries = input("Which size? (s,m,l) >>> ")
     if fries == "s":
          fries = input("Would you like to Mega-Size? (y,n) >>> ")
          if fries =="y":
               fries = "l"
               total += 2.00
          else:
               fries= "s"
               total += 1.00
     elif fries == "m":
          total += 1.75
     elif fries == "l":
          total += 2.00
     orderInformation+=(f"\tFries:\t\t{fries}\n")

#Iteration 4
ketchup = int(input("How many ketchup packets do you want? ($.25/per) >>> "))
total += ketchup*.25
orderInformation += f"\tKetchup:\t{ketchup}\n"

if chooseDrink and chooseFries and chooseSandwich:
     total-=1

#https://www.w3schools.com/python/ref_func_round.asp
orderInformation += f"\tSubtotal: $\t{round(total, 2)}\n\tTotal: $\t{round(total + (total * 0.07), 2)}\n"
print(orderInformation)

"""
print(f'''
Your order:
     Sandwich:  {sandwich}
     Drink:     {drink}
     Fries:     {fries}
     Ketchup:   {ketchup}
     Subtotal: ${total}

''')
"""