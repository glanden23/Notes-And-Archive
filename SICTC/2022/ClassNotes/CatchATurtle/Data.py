from random import randint

file = open("leaderboard.txt","a")
for i in range(1001):
    file.write(f"User{i},{randint(0, 25)}\n")