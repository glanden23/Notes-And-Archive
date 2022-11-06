import random
amountOfNumbers = 10
smallest = 0
biggest = 100000

def giveMeSomeNumbers(amountOfNumbers, smallest, biggest):
    listy=[]
    # Create a list of 10 random numbers
    for i in range(amountOfNumbers):
        listy.append(random.randint(smallest,biggest))
    return listy

def averageOfList(numbers):
    return sum(numbers) / len(numbers)

def amountOfPrimes(numbers):
    primes = 0
    for i in numbers:
        if i%2==0:
            primes+=1
    return primes

numbers = giveMeSomeNumbers(amountOfNumbers, smallest, biggest)

print("Average: "+ str(averageOfList(numbers)))
print("Biggest: " + str(max(numbers)))
print("Smallest: " + str(min(numbers)))
print("Sum: " + str(sum(numbers)))
print("Primes: " + str(amountOfPrimes(numbers)))