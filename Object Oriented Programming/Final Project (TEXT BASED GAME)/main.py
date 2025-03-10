# Created by Ali Adnan
# CMP621A
# February 21st 2025
# PROJECT TEXT BASED GAME

import time
from characters import *

# Global Variables
username = ""
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
    global username
    print("\nUNKNOWN: You're awake")
    SleepExtended()
    print("YOU: I am?")
    SleepExtended()
    print("UNKNOWN: God, I don't think you remember a thing")
    SleepExtended()
    print("YOU: What happened?")
    SleepExtended()
    print("UNKNOWN: He got to you...")
    SleepExtended()
    print("YOU: Who Did?")
    SleepExtended()
    print("UNKNOWN: The Master. He betrayed you")
    SleepExtended()
    print("YOU: Oh, He stole the sword as well")
    SleepExtended()
    print("UNKNOWN: THE Sword?")
    SleepExtended()
    print("YOU: THE Sword.")
    SleepExtended()
    print("UNKNOWN: What's your name, partner?")
    username = input("Type in your name: ")
    print(f"{username}: The name's {username}, and you are?")
    SleepExtended()
    print("ALLOY: I'm Alloy. I found you lying in the woods after you were betrayed. Thought you were dead.")
    SleepExtended()
    print(f"{username}: Well then, I suppose I can either continue to lie here or avenge myself.")
    SleepExtended()
    print("-----------DIALOGUE END-----------")

def MidScene():
    print("ALLOY: I will be your personal sidekick as you go through this journey.")
    SleepExtended()
    print("ALLOY: Whenever you need advice, select the number that corresponds with me.")
    SleepExtended()
    print(f"ALLOY: Good luck, {username}.")
    SleepExtended()

def Scene1():
    SafeZone()

def Fight():
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
                combat_item = "Sword"
            elif battleinput == 2:
                combat_item = "Shield"
            elif battleinput == 3:
                combat_item = "Potion"
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

# Character Build
def BuildPick():
    global MAINCHARACTER
    print("Select your initial build:")
    print("1 - 150 Health, 60 Strength, 20XP")
    print("2 - 100 Health, 80 Strength, 40XP")
    print("3 - 80 Health, 120 Strength, 30XP")
    buildinput = int(input("Pick a number: "))
    if buildinput == 1:
        MAINCHARACTER = MainCharacters(username, 150, 60, 20)
    elif buildinput == 2:
        MAINCHARACTER = MainCharacters(username, 100, 80, 40)
    elif buildinput == 3:
        MAINCHARACTER = MainCharacters(username, 80, 120, 30)
    else:
        print("Invalid choice. Defaulting to build 1.")
        MAINCHARACTER = MainCharacters(username, 150, 60, 20)
    print(f"Your character {MAINCHARACTER.Name} has been built with these features")
    MAINCHARACTER.tell()
    print(MAINCHARACTER)

def TravelFromSafeZone():
    while True:
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

def TravelFromHiddenDungeon():
    while True:
        print ("You are currently in the hidden dungeon (North)")
        userinput = int(input("1 - Go Forward (The Master's Lair)"))
        if userinput == 1:
            TheMastersLair()
        else:
            print("Invalid input, try again.")

def SafeZone():
    global SafeZoneDiscovered
    SafeZoneDiscovered = True
    print("UNKNOWN: Oh, new guest! How's it going?")
    Sleep()
    print(f"{username}: Hey! I have no idea where I'm at? I'm {username}")
    Sleep()
    print("LLOYD: Hello, Welcome to my safe zone. I'm Lloyd and you can always find me here for resources and help.")
    Sleep()
    TravelFromSafeZone()

def TheWoods():
    global TheWoodsDiscovered
    TheWoodsDiscovered = True
    print("You have entered the woods.")
    print("You have encountered a foe.")
    Fight()

def TheVast():
    global TheVastDiscovered
    TheVastDiscovered = True
    print("You have entered the vast dungeon.")
    print("You have encountered a foe.")
    print("The foe whispers to you...")
    print("I know you, you will never get to the master. Quit while you can.")
    Fight()

def TheHiddenDungeon():
    print("You have entered the hidden dungeon.")
    print ("You lurk around to find whats so mysterious about this hidden dungeon.")
    print("You have encountered a foe.")
    Fight()
    print ("You keep moving forward and find a chest.")
    print ("You open the chest and find a letter.")
    print ("Letter reads, Leave my Lair while you still can... you will regret this")
    TravelFromHiddenDungeon()

def TheMastersLair():
    print("You have entered the Master's Lair.")
    print("You have encountered the Master.")
    print("The Master: You have come to face me, I see.")
    print(f"{MAINCHARACTER.Name}: I have come to take back what is mine.")
    print("The Master: You will never get the sword back.")
    print(f"{MAINCHARACTER.Name}: I will take it back, even if it means I have to fight you.")
    print("The Master: You will regret this.")
    Fight()





def Game():
    IntroScene()
    BuildPick()
    MidScene()
    Scene1()

def Menu():
    while True:
        print("1- Start Game")
        print("2- High Score")
        print("3- Credits")
        print("4- Quit Game")
        menuinp = int(input("Please select a menu option: "))
        if menuinp == 1:
            Game()
        elif menuinp == 2:
            print("High score feature not implemented yet.")
        elif menuinp == 3:
            print("Created / Coded By Ali Adnan")
            print("CMP621A - Andrew MacDougald")
            time.sleep(1)
        elif menuinp == 4:
            print("Thank you for playing.")
            break
        else:
            print("Invalid input, please try again.")

print("Ali Adnan Presents")
time.sleep(1)
print("The Master")
time.sleep(1)
Menu()
