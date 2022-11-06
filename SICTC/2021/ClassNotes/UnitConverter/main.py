from UnitConverter import UnitConverter

UI = f'''
    1 - convert f to c
    2 - convert f to k
    3 - convert c to f
    4 - convert c to k
    5 - convert k to c
    6 - convert k to f
    q - quit
'''

print(UI)
u = input(">>> ")
while(u!="q"):
    if u=="1":
        print(UnitConverter.fahrenheitToCelsius(int(input("Fahrenheit >>> "))))
    elif u=="2":
        print(UnitConverter.fahrenheitToKelvin(int(input("Fahrenheit >>> "))))
    elif u=="3":
        print(UnitConverter.celsiusToFahrenheit(int(input("Celsius >>> "))))
    elif u=="4":
        print(UnitConverter.celsiusToKelvin(int(input("Celsius >>> "))))
    elif u=="5":
        print(UnitConverter.kelvinToCelsius(int(input("Kelvin >>> "))))
    elif u=="6":
        print(UnitConverter.kelvinToFahrenheit(int(input("Kelvin >>> "))))
    print(UI)
    u = input(">>> ")
print("Goodbye.")