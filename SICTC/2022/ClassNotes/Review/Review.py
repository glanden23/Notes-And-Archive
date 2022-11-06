#loops...
# for loop
'''
s = "This is the power of python."
for letter in "Hello World":
    print(letter)
for i in range(len(s)):
    print(s[i])

sL = list(s)

#find the index of p
for i in range(len(sL)):
    if sL[i] == "p":
        print("Found p in index: " + str(i))
        sL[i] = "y"
#cheater
#print("".join(sL))

#join string
def listToString(listVar):
    out = ""
    for eachLetter in listVar:
        out += eachLetter
    return out
print(listToString(sL))'''

# while loop

s="seahorse"
#print the indexes of the vowels using while loop
vowels = "aeiou"
c = 0
while c != len(s):
    if s[c].lower() in vowels:
        print(f"Found {s[c]} with index of {c}.")
    c+=1

'''
awake = "no"
while awake.lower() == "no":
    awake = input("Are you awake? >>> ")
    
amount = 0
while amount < 90000:
    amount+=1
print("Looped 90,000 times.")'''