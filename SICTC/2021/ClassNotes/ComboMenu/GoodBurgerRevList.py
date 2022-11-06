#Iteration 1
total=0
order=["none","none","none","none"]
orderInformation = "\nYour Order:\n"
chooseSandwich,chooseFries,chooseDrink = False,False,False

sandwich = input("Would you like a drink? (y,n) >>> ")
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
     order[0] = sandwich

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
               drink="c"
          else:
               total += 2.25
               drink="l"
     orderInformation+=(f"\tDrink:\t\t{drink}\n")
     order[1] = drink
     

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
     order[2] = fries

#Iteration 4
ketchup = int(input("How many ketchup packets do you want? ($.25/per) >>> "))
total += ketchup*.25
order[3] = ketchup
orderInformation += f"\tKetchup:\t{ketchup}\n"

print(order)

#if chooseDrink and chooseFries and chooseSandwich:
#     total-=1

#checks if something is not in list.
if not("none" in order):
     total-=1

orderInformation += f"\tSubtotal: $\t{total}\n"
#print(orderInformation)

print(f'''
Your order:
     Sandwich:  {order[0]}
     Drink:     {order[1]}
     Fries:     {order[2]}
     Ketchup:   {order[3]}
     Subtotal: ${round(total, 2)}
     Total:    ${round(total + (total * 0.07), 2)}
''')