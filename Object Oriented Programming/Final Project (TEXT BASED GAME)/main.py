# Created by Ali Adnan
# CMP621A
# February 21st 2025
# PROJECT TEXT BASED GAME

import time
import random
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
    print("")

def Scene1():
    SafeZoneScene()
    print("")
    SafeZone()

def Fight():
    while True:
        print("1 - Talk")
        print("2 - Battle")
        print("3 - Flee")
        userinput = int(input("Select a choice: "))

        if userinput == 1:
            randint=random.randint(1, 3)
            if randint == 1:
                print(f"{MAINCHARACTER.Name}: Hey, I'm {MAINCHARACTER.Name}, I'm just passing through")
                print("FOE: I don't care who you are dude, my sole purpose is attacking you")
                print(f"{MAINCHARACTER.Name}: Is there any way I can win you over?")
                print("FOE: No, just no.")
            elif randint == 2:
                print(f"{MAINCHARACTER.Name}: Hey, I'm {MAINCHARACTER.Name}, I'm just passing through")
                print("FOE: I don't care who you are dude, my sole purpose is attacking you")
                print(f"{MAINCHARACTER.Name}: Can we talk this out?")
                print("FOE: No, just no.")
            elif randint == 3:
                print(f"{MAINCHARACTER.Name}: Hey, I'm {MAINCHARACTER.Name}, I'm just passing through")
                print("FOE: I don't care who you are dude, my sole purpose is attacking you")
                print(f"{MAINCHARACTER.Name}: Can we be friends?")
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
            randint = random.randint(1, 4)
            if randint == 1:
                print("You have defeated the foe, gained Strength and XP")
                MAINCHARACTER.Strength += 10
                MAINCHARACTER.XP += 10
            elif randint ==2:
                print("You have been defeated by the foe, Lost health and XP")
                MAINCHARACTER.Health -= 10
                MAINCHARACTER.XP -= 10
            elif randint == 3:
                print("You have defeated the foe, gained Strength and XP")
                MAINCHARACTER.Strength += 20
                MAINCHARACTER.XP += 20
            elif randint == 4:
                print("You have been defeated by the foe, Lost health and XP")
                MAINCHARACTER.Health -= 20
                MAINCHARACTER.XP -= 20
            break  # Exit loop after battle
        elif userinput == 3:
            randint = random.randint(1, 2)
            if randint == 1:
                print("You have fled the foe")
            elif randint == 2:
                print ("The Foe got to you, lost health and XP")
                MAINCHARACTER.Health -= 10
                MAINCHARACTER.XP -= 10
            break  # Exit loop after fleeing
        else:
            print("Invalid choice, try again.")

def FinalFight():
    print("What would you like to battle the Master with?")
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
    print(f"You have chosen the {combat_item}")
    randint = random.randint(1, 2)
    if randint == 1:
        print("You hit the master with the sword, and damage him severely")
        print("The Master: You will regret this.")
    elif randint == 2:
        print("The Master hits you with a spell, you lose health and XP")
        MAINCHARACTER.Health -= 30
        MAINCHARACTER.XP -= 30
    if MAINCHARACTER.Health <= 0:
        print("You have been defeated by the Master.")
        print("GAME OVER")
        exit()
    

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
            break
        elif userinput == 2:
            TheWoods()
            break
        elif userinput == 3:
            if statusunlocked:
                TheHiddenDungeon()
                break
            else:
                print("You have not unlocked this zone yet! Discover all areas to unlock")
        else:
            print("Invalid Input, Try again.")

def TravelFromHiddenDungeon():
    while True:
        print ("You are currently in the hidden dungeon (North)")
        userinput = int(input("1 - Go Forward (The Master's Lair)"))
        if userinput == 1:
            TheMastersLair()
        else:
            print("Invalid input, try again.")

def TravelFromTheWoods():
    while True:
        print("You are currently in the woods (East)")
        userinput = int(input("1 - Go West (Safe Zone)\n2- Go North (The Vast Dungeon)\nMake your Choice: "))
        if userinput == 1:
            SafeZone()
            break
        elif userinput == 2:
            TheVast()
            break
        else:
            print("Invalid Input, Try again.")

def TravelFromTheVast():
    while True:
        print("You are currently in the vast dungeon (West)")
        userinput = int(input("1 - Go East (Safe Zone)\n2- Go South (The Woods)\nMake your Choice: "))
        if userinput == 1:
            SafeZone()
            break
        elif userinput == 2:
            TheWoods()
            break
        else:
            print("Invalid Input, Try again.")

def SafeZoneScene():
    global SafeZoneDiscovered
    SafeZoneDiscovered = True
    print("UNKNOWN: Oh, new guest! How's it going?")
    SleepExtended()
    print(f"{username}: Hey! I have no idea where I'm at? I'm {username}")
    SleepExtended()
    print("LLOYD: Hello, Welcome to my safe zone. I'm Lloyd, the owner of this place. Feel free to come by here to rest.")
    SleepExtended()

def SafeZone():
    while True:
        print("You have entered the safe zone.")
        print("What would you like to do?")
        print("1 - Ask Lloyd For Advice")
        print("2 - Travel")
        print("3 - Talk to alloy")
        userinput = int(input("Select a choice: "))
        if userinput == 1:
            ranint=random.randint(1, 3)
            if ranint == 1:
                print ("Lloyd: You should go to the vast dungeon first, it's the closest to you and will teach you things.")
            elif ranint == 2:
                print ("Lloyd: You should go to the woods, Heard its a cool spot! but watch out...")
            elif ranint == 3:
                print ("Lloyd: The hidden dungeon, its a mysterious place. Some say its a myth. but The only way you can find out is by going")
        elif userinput == 2:
            TravelFromSafeZone()
            break
        elif userinput == 3:
            print (f"ALLOY: Hey {username}! You are currently in the Safe Zone, nothing can harm you. You can choose to rest here and brainstorm or you can continue your adventure")

def TheWoods():
    global TheWoodsDiscovered
    TheWoodsDiscovered = True
    print("You have entered the woods.")
    print("You have encountered a foe.")
    Fight()
    print("You continue to stroll through the woods. Nothing seems to be out of the ordinary.")
    print("You have found a chest.")
    print("You open the chest and find a letter.")
    print("Letter reads, You will never find me, you will never get the sword back.")
    print("The woods has been discovered, you are one step further to unlocking the hidden dungeon")
    print("What would you like to do now?")
    print("1 - Continue to explore (encounter foe and gain strength)")
    print("2 - Travel")
    userinput = int(input("Select a choice: "))
    if userinput == 1:
        print("You continue to explore the woods.")
        print("You have encountered a foe.")
        Fight()
    elif userinput == 2:
        TravelFromTheWoods()

def TheVast():
    global TheVastDiscovered
    TheVastDiscovered = True
    print("You have entered the vast dungeon.")
    print("You have encountered a foe.")
    print("The foe whispers to you...")
    print("I know you, you will never get to the master. Quit while you can.")
    Fight()
    print("You keep moving forward")
    print ("The Dungeon is as vast as it can be, you keep moving forward and encounter another foe")
    Fight()
    print("You find the last true key to the hidden dungeon")
    print("You have discovered the vast dungeon, you are one step further to unlocking the hidden dungeon")
    print("What would you like to do now?")
    print("1 - Continue to explore (encounter foe and gain strength)")
    print("2 - Travel")
    userinput = int(input("Select a choice: "))
    if userinput == 1:
        print("You continue to explore the vast dungeon.")
        print("You have encountered a foe.")
        Fight()
    elif userinput == 2:
        TravelFromTheVast()

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
    SleepExtended()
    print(f"{MAINCHARACTER.Name}: I have come to take back what is mine.")
    SleepExtended()
    print("The Master: You will never get the sword back.")
    SleepExtended()
    print(f"{MAINCHARACTER.Name}: I will take it back, even if it means I have to fight you.")
    SleepExtended()
    print("The Master: You will regret this.")
    FinalFight()





def Game():
    IntroScene()
    BuildPick()
    MidScene()
    Scene1()

def Menu():
    while True:
        print("1- Start Game")
        print("2- Credits")
        print("3- Quit Game")
        menuinp = int(input("Please select a menu option: "))
        if menuinp == 1:
            Game()
        elif menuinp == 2:
            print("Created / Coded By Ali Adnan")
            print("CMP621A - Andrew MacDougald")
            time.sleep(1)
        elif menuinp == 3:
            print("Thank you for playing.")
            break
        else:
            print("Invalid input, please try again.")

print("Ali Adnan Presents")
time.sleep(1)
print("The Master")
time.sleep(1)
Menu()
