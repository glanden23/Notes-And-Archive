import random
import time
from os.path import exists

def databaseStartup():
    file = exists('./RPGData.data')
    if file == False:
        #https://www.w3schools.com/python/ref_func_open.asp
        open("./RPGData.data", "w+")
        return True
    else:
        return False

def databaseInput(search, value):
    file = open('./RPGData.data', "r")
    data = file.read()
    if search in data:
        datalist = data.split(" | ")
        for x in range(len(datalist)):
            if datalist[x].startswith(search):
                datalist[x] = search+": "+value
                file = open('./RPGData.data', "w")
                newdata = " | ".join(datalist)
                file.write(newdata)
    else:
        file = open('./RPGData.data', "w")
        file.write(data+search+": "+value+" | ")

def databaseOutput(search):
    file = open("./RPGData.data", "r")
    data = file.read()
    if search in data:
        datalist = data.split(" | ")
        for x in range(len(datalist)):
            if datalist[x].startswith(search):
                value = datalist[x].split(": ")
                return value[1]

def clearScreen():
    print("\n"*1000)

def newPlayerName():
    clearScreen()
    print("Welcome new player! What would you like your name to be?")
    ui = input(">>> ")
    while len(ui) > 20:
        print("Name is too long.")
        ui = input(">>> ")
    databaseInput("Name", ui)
    databaseInput("NewPlayer", "False")
    databaseInput("Health", "100")
    databaseInput("MaxHealth", "100")
    databaseInput("Attack", "5")
    databaseInput("Money", "100")
    print("Welcome " + ui + "! Let's began, shall we?")

#
# PLAYER HOME INTERACTION
#

def playerHome():
    clearScreen()
    print(f"""
-=-=-=- Welcome to your home {databaseOutput("Name")}! -=-=-=-
Your Stats:
- Health: {databaseOutput('Health')}/{databaseOutput('MaxHealth')}
- Attack: {databaseOutput('Attack')}
Current Balance:
- Money: ${databaseOutput('Money')}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
    ui = input("When you are ready to leave, press enter.\nIf you want to heal health, type \"h\".\n>>> ")
    if ui.lower() == "h":
        while int(databaseOutput('MaxHealth')) >= int(databaseOutput('Health')):
            databaseInput("Health", str(int(databaseOutput('Health')) + 100))
            time.sleep(0.5)
            print("+100 Health")
        databaseInput("Health", str(int(databaseOutput('MaxHealth'))))
        print("You are max health!")
        time.sleep(3)
        playerHome()
    else:
        whereTo()

#
# WHERE TO INTERACTION
#

def whereTo():
    clearScreen()
    print(f"""
-=-=-=- Where would you like to go? -=-=-=-
1. Home
2. Wilderness
3. Shop
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
    ui = input(">>> ")
    if ui.isdigit():
        ui = int(ui)
        if ui == 1:
            playerHome()
        elif ui == 2:
            WildLog = ["You've began your adventure!"]
            Wilderness(WildLog)
        elif ui == 3:
            shop()
        else:
            print("Not an option.")
            whereTo()
    else:
        whereTo()

#
# WILDERNESS INTERACTIONS
#

def wildWait(wait,log):
    dots = 0
    while wait > 0:
        wait = wait - 1
        clearScreen()
        print("\n".join(log))
        if dots == 0:
            dots = 1
            print("...")
            time.sleep(1)
        elif dots == 1:
            dots = 2
            print("..")
            time.sleep(1)
        elif dots == 2:
            dots = 0
            print(".")
            time.sleep(1)

#
# BATTLE INTERACTION
#

def battle(enemy, enemyhealth, enemyattack):
    clearScreen()
    health = int(databaseOutput("Health"))
    databaseInput("Health", str(health - enemyattack))
    health = int(databaseOutput("Health"))
    maxhealth = int(databaseOutput("MaxHealth"))
    attack = int(databaseOutput("Attack"))
    print(f"""
-=-=-=- BATTLE -=-=-=-
{enemy}:
* Health: {enemyhealth}
* Attack: {enemyattack}
-=-=-=-=-=-=-=-=-=-=-
{databaseOutput("Name")}:
* Health: {health}/{maxhealth}
* Attack: {attack}
-=-=-=-=-=-=-=-=-=-=-
The {enemy} hit you for {enemyattack}!
-=-=-=-=-=-=-=-=-=-=-
What would you like to do?
1. Attack, 2. Run
-=-=-=-=-=-=-=-=-=-=-""")
    if health <= 0:
        print("You died and lost " + databaseOutput("Money"))
        databaseInput("Money", "0")
        return
    ui = input(">>> ")
    if ui.isdigit():
        ui = int(ui)
        if ui == 1:
            if enemyhealth - attack <= 0:
                if "Boss" in enemy:
                    earned = random.randint(250, 500) + (int(databaseOutput("Health")) * random.random())
                else:
                    earned = random.randint(100, 250) + (int(databaseOutput("Health")) * random.random())
                databaseInput("Money", str(int(databaseOutput("Money")) + earned))
                print("You won and earned " + str(earned) + " gold!")
                time.sleep(3)
                return
            print("You hit " + enemy + " for " + str(attack) + " damage!")
            time.sleep(3)
            battle(enemy, enemyhealth - attack, enemyattack)
        elif ui == 2:
            if random.randint(0, 3) == 0:
                print("You got away!")
                time.sleep(3)
            else:
                print("You didn't manage to escape...")
                time.sleep(3)
                battle(enemy, enemyhealth, enemyattack)
        else:
            print("You missed your hit! (make sure you enter 1 - 2)")
            time.sleep(3)
            battle(enemy, enemyhealth, enemyattack)
    else:
        print("You missed your hit! (make sure you enter 1 - 2)")
        time.sleep(3)
        battle(enemy, enemyhealth, enemyattack)

def explore(place):
    clearScreen()
    exploreLog = []
    health = int(databaseOutput("Health"))
    maxhealth = int(databaseOutput("MaxHealth"))
    exploreLog.append("You entered the " + place + "...")
    wildWait(random.randint(3, 6), exploreLog)
    doorTrapped = random.randint(0, 1)
    if doorTrapped == 1:
        databaseInput("Health", str(health - 10))
        health = int(databaseOutput("Health"))
        if health <= 0:
            exploreLog.append(f"The door was trapped and you died.. losing {databaseOutput('Money')}...")
            databaseInput("Money", "0")
            wildWait(random.randint(3, 6), exploreLog)
            return
        exploreLog.append(f"The door was trapped! {health}/{maxhealth}")
        wildWait(random.randint(3, 6), exploreLog)
    lootAmount = range(random.randint(0, 3))
    for i in lootAmount:
        chestOrGold = random.randint(0, 1)
        if chestOrGold == 0:
            exploreLog.append("You found a chest, do you want to open it?")
            wildWait(1, exploreLog)
            ui = input("(y,n) >>> ")
            if ui == "y":
                chestChance = random.randint(0, 1)
                if chestChance == 0:
                    databaseInput("Health", str(health - 20))
                    health = int(databaseOutput("Health"))
                    if health <= 0:
                        exploreLog.append(f"The chest was trapped and you died.. losing {databaseOutput('Money')}...")
                        databaseInput("Money", "0")
                        wildWait(random.randint(3, 6), exploreLog)
                        return
                    exploreLog.append(f"The chest was trapped! {health}/{maxhealth}")
                    wildWait(random.randint(3, 6), exploreLog)
                else:
                    exploreLog.append("You opened the chest...")
                    wildWait(random.randint(3, 6), exploreLog)
                    amount = random.randint(50, 250)
                    databaseInput("Money", str(int(databaseOutput("Money")) + amount))
                    exploreLog.append("You found " + str(amount) + " gold in the chest!")
                    wildWait(random.randint(3, 6), exploreLog)
            else:
                exploreLog.append("You left the chest behind...")
                wildWait(random.randint(3, 6), exploreLog)
        else:
            amount = random.randint(25, 100)
            databaseInput("Money", str(int(databaseOutput("Money")) + amount))
            exploreLog.append("You found " + str(amount) + " gold lying around...")
            wildWait(random.randint(3, 6), exploreLog)
    exploreLog.append("You didn't find anything else.")
    wildWait(random.randint(3, 6), exploreLog)

    

def Wilderness(log):
    health = int(databaseOutput("Health"))
    if health <= 0:
        playerHome()
        return
    clearScreen()
    ui = input("Are you sure you want to continue? (y,n) >>> ")
    if ui.lower() == "n":
        playerHome()
        return
    wildWait(random.randint(3, 6), log)
    chance = random.randint(0, 10)
    if chance <= 5:
        enemyTypes = ["Goblin", "Zombie", "Slime", "Bander", "Stalker", "Bat", "Mutant", "Spider", "Demon"]
        randomizer = random.random()
        enemyHealth = int(randomizer * (int(databaseOutput("Health")) / 3))
        enemyAttack = int(randomizer * (int(databaseOutput("Attack"))))
        if (randomizer == 2):
            enemyName = "Boss " + enemyTypes[random.randint(0, len(enemyTypes) - 1)]
        else:
            enemyName = enemyTypes[random.randint(0, len(enemyTypes) - 1)]
        log.append("You ran into a " + enemyName + "!")
        battle(enemyName, enemyHealth, enemyAttack)
        Wilderness(log)
    else:
        placeName = ["Abandoned House", "Mineshaft", "Dead Titan Golem", "Hollow Rotting Tree", "Abandoned Cave", "Broken Watermill"]
        place = placeName[random.randint(0, len(placeName) - 1)]
        explore(place)
        log.append("You went into a " + place)
        Wilderness(log)

    

#
# SHOP INTERACTIONS
#

def shopBuy():
    clearScreen()
    money = int(databaseOutput("Money"))
    health = int(databaseOutput("MaxHealth"))
    attack = int(databaseOutput("Attack"))
    print(f"""
-=-=-=- Upgrade! -=-=-=-
1. Health: {health} -> {health + 10} (${health})
2. Attack: {attack} -> {attack + 5} (${attack * 100})
3. Leave
-=-=-=-=-=-=-=-=-=-=-=-=-
Balance: ${money}""")
    ui = input(">>> ")
    if ui.isdigit():
        ui = int(ui)
        if ui == 1:
            if money >= health:
                databaseInput("Money",str(money - health))
                databaseInput("MaxHealth",str(health + 10))
                shopBuy()
            else:
                print("You don't have enough money!")
                time.sleep(3)
                shopBuy()
        elif ui == 2:
            if money >= attack * 100:
                databaseInput("Money",str(money - attack * 100))
                databaseInput("Attack",str(attack + 5))
                shopBuy()
            else:
                print("You don't have enough money!")
                time.sleep(3)
                shopBuy()
        elif ui == 3:
            shop()
        else:
            shopBuy()
    else:
        shopBuy()

def shopSell():
    clearScreen()
    money = int(databaseOutput("Money"))
    health = int(databaseOutput("MaxHealth"))
    attack = int(databaseOutput("Attack"))
    print(f"""
-=-=-=- Downgrade! -=-=-=-
1. Health: {health} -> {health - 10} (+${health - 20})
2. Attack: {attack} -> {attack - 5} (+${attack * 100 - 20})
3. Leave
-=-=-=-=-=-=-=-=-=-=-=-=-=-
Balance: ${money}""")
    ui = input(">>> ")
    if ui.isdigit():
        ui = int(ui)
        if ui == 1:
            if health > 100:
                databaseInput("Money",str(money + health - 20))
                databaseInput("MaxHealth",str(health - 10))
                if health - 10 < int(databaseOutput("Health")):
                    databaseInput("Health", str(health - 10))
                shopSell()
            else:
                print("You can't downgrade your health, its too low!")
                time.sleep(3)
                shopSell()
        elif ui == 2:
            if attack > 5:
                databaseInput("Money",str(money + (attack * 100 - 20)))
                databaseInput("Attack",str(attack - 5))
                shopSell()
            else:
                print("You can't downgrade your attack, its too low!")
                time.sleep(3)
                shopSell()
        elif ui == 3:
            shop()
        else:
            shopSell()
    else:
        shopSell()

def shop():
    clearScreen()
    print(f"""
-=-=-=- What would you like to do? -=-=-=-
1. Upgrade
2. Downgrade
3. Leave
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
    ui = input(">>> ")
    if ui.isdigit():
        ui = int(ui)
        if ui == 1:
            shopBuy()
        elif ui == 2:
            shopSell()
        elif ui == 3:
            whereTo()
        else:
            shop()
    else:
        shop()

if __name__ == "__main__":
    newPlayer = databaseStartup()
    if newPlayer == True:
        databaseInput("NewPlayer", 'True')
    if databaseOutput("NewPlayer") == "True":
        newPlayerName()
    playerHome()