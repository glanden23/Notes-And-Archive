print("Input a list of random things and see how it turns out in the story!")
inputList = [input("Input a name. >>> "),input("Input an animal. >>> "),input("Input a type of transporation. >>> "),input("Input a planet name. >>> "), input("Input an object. >>> "), input("Input an object. >>> "), input("Input a name. >>> "),input("Input a direction. >>> "), input("Input a name. >>> "),input("Input a name. >>> "),input("Input an action. >>> "),input("Input an event. >>> ")];
print(f"""
{inputList[0]} was riding a {inputList[1]} which was riding a 
{inputList[2]} on the planet {inputList[3]} when a {inputList[4]}
hit them off {inputList[3]} and they went flying into a {inputList[5]}.
In the {inputList[5]} they found {inputList[6]} who told them they
needed to go {inputList[7]}. When they went {inputList[7]} they found
a {inputList[2]} riding contest and joined in. They asked {inputList[8]} and {inputList[9]}
to help them win. They came up with a masterful plan...\n\nWhen the race started they would {inputList[10]} {inputList[0]} and he would {inputList[11]} and win!""")