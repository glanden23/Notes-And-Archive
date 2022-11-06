import random
import math
print("Insert number of points:")
np = input()
while not np.isdigit():
        print("Insert number of points:")
        np = input()
np = int(np)
length = 300

inside = 0
outside = 0
for i in range(0,np):
    x = random.uniform(0,length)
    y = random.uniform(0,length)
    d = math.sqrt(x**2 + y**2)
    if d <= length:
            inside += 1
    else:
            outside += 1

print(inside, np,(inside/np)*4.0)