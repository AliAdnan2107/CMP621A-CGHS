# Created by Ali Adnan
# CMP621A
# February 21st 2025
# PROJECT TEXT BASED GAME

import time
from characters import *

# Global Variables
global username
global statusunlocked
statusunlocked = False
SafeZoneDiscovered = False
TheWoodsDiscovered = False
TheVastDiscovered = False

# Utility Functions
def Sleep():
    time.sleep(1)

def SleepExtended():
    time.sleep(1.5)

def NorthUnlock():
    global statusunlocked
    if SafeZoneDiscovered and TheWoodsDiscovered and TheVastDiscovered:
        statusunlocked = True

# Scenes
def IntroScene():
    print("\nUNKNOWN: You're awake")
    SleepExtended()
    print("YOU: I am?")
    SleepExtended()
    print("UNKNOWN: God I don't think you remember a thing")
    SleepExtended()
    print("YOU: What happened?")
    SleepExtended()
    print("UNKNOWN: He got to you...")
    SleepExtended()
    print("YOU: Who Did?")
    SleepExtended()
    print("UNKNOWN: The Master. He Betrayed you")
    SleepExtended()
    print("YOU: Oh, He stole the sword as well")
    SleepExtended()
    print("UNKNOWN: THE Sword?")
    SleepExtended()
    print("YOU: THE Sword.")
    SleepExtended()
    print("UNKNOWN: What's your name partner?")
    global username
    username = input("Type in your name: ")
    print(f"{username}: The Name's {username}, and you are?")
    SleepExtended()
    print("ALLOY: I'm Alloy, I found you lying in the woods after you were betrayed I assume. Thought you were dead.")
    SleepExtended()
    print(f"{username}: Well then, I suppose I can either continue to lie here or Avenge myself.")
    SleepExtended()
    print("-----------DIALOGUE END-----------")

def MidScene():
    print("ALLOY: I will be your personal sidekick as you go through this journey.")
    SleepExtended()
    print("ALLOY: Whenever you need advice, Select the number that corresponds with me")
    SleepExtended()
    print(f"ALLOY: Good Luck, {username}.")
    SleepExtended()
    print ("")

def Scene1():
    SafeZone()

# Character Build
def BuildPick():
    print("Select your initial build:")
    print("1 - 150 Health, 60 Strength, 20XP")
    print("2 - 100 Health, 80 Strength, 40XP")
    print("3 - 80 Health, 120 Strength, 30XP")
    buildinput = int(input("Pick a number: "))
    global MAINCHARACTER
    if buildinput == 1:
        MAINCHARACTER = MainCharacters(username, 150, 60, 20)
    elif buildinput == 2:
        MAINCHARACTER = MainCharacters(username, 100, 80, 40)
    elif buildinput == 3:
        MAINCHARACTER = MainCharacters(username, 80, 120, 30)
    else:
        return
    print ("")
    print(f"Your Character {MAINCHARACTER.Name} has been built with these features")
    MAINCHARACTER.tell()
    print(MAINCHARACTER)

def Fight(self, combat_item):
    while True:
        print("1 - Talk")
        print("2 - Battle")
        print("3 - Flee")
        userinput = int(input("Select a choice: "))
        if userinput == 1:
            print(f"{MAINCHARACTER.Name}: Hey, I'm {MAINCHARACTER.Name}, I'm just passing through")
            print("FOE: I don't care who you are dude, my sole purpose is attacking you")
            print(f"{MAINCHARACTER.Name}: Is there any way I can win you over?")
            print("FOE: No, just no.")

        elif userinput == 2:
            print("What would you like to battle the foe with?")
            print("1 - Sword")
            print("2 - Shield")
            print("3 - Potion")
            battleinput = int(input("Select a choice: "))

            if battleinput == 1:
                combat_item = Sword
            elif battleinput == 2:
                combat_item = Shield
            elif battleinput == 3:
                combat_item = Potion
            else:
                print("Invalid choice, try again.")
                continue

            print(f"You have chosen the {combat_item}")
            print("You have defeated the foe")
            break  # Exit loop after battle

        elif userinput == 3:
            print("You have fled the foe")
            break  # Exit loop after fleeing

        else:
            print("Invalid choice, try again.")


# Items
class Item:
    def __init__(self, name, item_type, damage=0, defense=0, healing_power=0):
        self.name = name
        self.item_type = item_type
        self.damage = damage
        self.defense = defense
        self.healing_power = healing_power
    def __str__(self):
        return f"{self.name} ({self.item_type})"

class Sword(Item):
    def __init__(self, name, damage):
        super().__init__(name, "Weapon", damage=damage)

class Shield(Item):
    def __init__(self, name, defense):
        super().__init__(name, "Armor", defense=defense)

class Potion(Item):
    def __init__(self, name, healing_power):
        super().__init__(name, "Consumable", healing_power=healing_power)

# Rooms
def SafeZone():
    global SafeZoneDiscovered
    SafeZoneDiscovered = True
    print("UNKNOWN: Oh, new guest! How's it going?")
    Sleep()
    print(f"{username}: Hey! I have no idea where I'm at? I'm {username}")
    Sleep()
    print("LLOYD: Hello, Welcome to my safe zone. I'm Lloyd and you can always find me here for resources and help")
    Sleep()
    SafeZoneShop = True
    while SafeZoneShop:
        print("1 - Acquire Resources")
        print("2 - Ask For Advice")
        print("3 - Leave to explore")
        print("4 - Talk to Alloy")
        userinput = int(input("Select a choice: "))
        if userinput == 1:
            print("LLOYD: What can I get you?")
            shopinput = int(input("1 - Additional Health\n2 - Additional Strength\n3 - Tools\nSelect a choice: "))
            if shopinput == 1:
                print ("LLOYD: Additional Health it is!")
                if MAINCHARACTER.XP>=20:
                    MAINCHARACTER.Health+=20
                    print (f"Your Health has increased by 20, you now have {MAINCHARACTER.Health} Health")
                else:
                    print ("LLOYD: You don't have enough XP for this, come back to me when you have earned more XP")
            elif shopinput == 2:
                print ("LLOYD: Additional Strength it is!")
                if MAINCHARACTER.XP>=40:
                    MAINCHARACTER.Strength+=20
                    print (f"Your Strength has increased by 20, you now have {MAINCHARACTER.Strength} Strength")
                else:
                    print ("LLOYD: You don't have enough XP for this, come back to me when you have earned more XP")
            elif shopinput == 3:
                print ("LLOYD: Tools it is!")
                print ("1 - Sword")
                print ("2 - Shield")
                print ("3 - Potion")
                input2=int(input("Select a choice: "))
                if input2==1:
                    print ("LLOYD: Sword it is!")
                    sword=Sword("Sword", 20)
                    print (f"You have acquired a {sword}")
                if input2==2:
                    print ("LLOYD: Shield it is!")
                    shield=Shield("Shield", 20)
                    print (f"You have acquired a {shield}")
                if input2==3:
                    print ("LLOYD: Potion it is!")
                    potion=Potion("Potion", 20)
                    print (f"You have acquired a {potion}")
        elif userinput == 2:
            print("LLOYD: You should explore the vast dungeon first, it's the easiest to navigate")
        elif userinput == 3:
            SafeZoneShop = False
            TravelFromSafeZone()

def TravelFromSafeZone():
    print("You are currently in the safe zone (South)")
    userinput = int(input("1 - Go West (Vast Dungeon)\n2- Go East (The Woods)\n3- Go North (The Hidden Dungeon)\nMake your Choice: "))
    if userinput == 1:
        TheVast()
    elif userinput == 2:
        TheWoods()
    elif userinput == 3:
        if statusunlocked:
            TheHiddenDungeon()
        else:
            print("You have not unlocked this zone yet! Discover all areas to unlock")
    else:
        print("You have not unlocked this zone yet! Discover all areas to unlock")

def TheWoods():
    global TheWoodsDiscovered
    TheWoodsDiscovered = True
    print("You have entered the woods")
    print("You have encountered a foe")
    Fight(MAINCHARACTER, Sword)

def TheVast():
    global TheVastDiscovered
    TheVastDiscovered = True

def TheHiddenDungeon():
    pass

def Game():
    IntroScene()
    BuildPick()
    MidScene()
    Scene1()

def Menu():
    while True:
        print ("1- Start Game")
        print ("2- High Score")
        print ("3- Credits")
        print ("4- Quit Game")
        menuinp=int(input("Please select a menu option: "))
        if menuinp==1:
            Game()
        elif menuinp==2:
            "high score"
        elif menuinp==3:
            print ("Created / Coded By Ali Adnan")
            print ("CMP621A - Andrew MacDougald")
            time.sleep(1)
        elif menuinp==4:
            print ("Thank you for playing")
            break
        else:
            "failsafe"

print("Ali Adnan Presents")
time.sleep(1)
print("The Master")
time.sleep(1)
Menu()