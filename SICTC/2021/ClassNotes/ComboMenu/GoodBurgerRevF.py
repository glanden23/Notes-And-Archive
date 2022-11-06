sandwich_index = 0
beverage_index = 1
fries_index = 2
ketchup_index = 3
keepOrdering=True
orderMasterList=[]
runningTotalPrintOut=""

def menuOptions(question,sizes,prices):
     total=0
     option = input(question)
     if option == "y":
          chooseOption=True
          option = input(f"Which size? {sizes} ")
          if option == sizes[0]:
               total+=prices[0]
          elif option == sizes[1]:
               total+=prices[1]
          elif option == sizes[2]:
               total+=prices[2]
          elif option == sizes[3]:
               total+=prices[3]
     else:
         chooseOption=False

     return (option,total,chooseOption)


while(keepOrdering):
     chooseSandwich,chooseFries,chooseDrink = False,False,False
     order = ["", "", "", 0]
     total=0
     orderInformation = "\nYour Order:\n"

     sandwich = input("Which sandwich would you like:  chicken $5.25, beef $6.25, tofu $5.75 ")
     if sandwich=="c" or sandwich=="b" or sandwich=="t":
          orderInformation+=(f"\tSandwich:\t{sandwich}\n")
          order[sandwich_index]=sandwich   #replace whatever is in the order list
          chooseSandwich=True
     if sandwich == "c":
          total+=5.25
     elif sandwich == "b":
          total+=6.25
     elif sandwich == "t":    #needs to be an elif because if I spell it wrong, it will charge 5.75
          total+=5.75

     #iteration 2
     drinkSelection = menuOptions("Would you like a drink? (y,n) ",["s","m","l","c"],[1,1.75,2.25,2.25+.38])
     order[beverage_index]=drinkSelection[0]
     total+=drinkSelection[1]
     chooseDrink=drinkSelection[2]

     #iteration 3
     q="Would you like a fries? (y,n) "
     s=["s","m","l","mega"]
     p=[1,1.75,2.00,2.00]
     friesSelection = menuOptions(q,s,p)
     order[beverage_index]=drinkSelection[0]
     total+=drinkSelection[1]
     chooseDrink=drinkSelection[2]

     #iteration 4
     ketchup = int(input("How many ketchup packets do you want? ($.25 ea) "))
     total+= (ketchup*.25)
     orderInformation+=(f"\tKetchup:\t{ketchup}\n")
     order[ketchup_index]=ketchup   #replace whatever is in the order list

     #if in our list a "" exist
     if not("" in order):
          total-=1
     #in checks to see if the item on left is in the item on right

     orderInformation+=(f"\tSubtotal: $\t{total}\n")
     # print(orderInformation)

     orderPrintOut = f'''
     Your order:
          Sandwich:  {order[sandwich_index]}
          Drink:     {order[1]}
          Fries:     {order[2]}
          Ketchup:   {order[3]}
          Subtotal: ${total}
     '''

     orderMasterList.append(order)
     runningTotalPrintOut += orderPrintOut

     if (input("Do you have another order? (y/n)")=="n"):
          keepOrdering=False


print(orderMasterList)
print(runningTotalPrintOut)