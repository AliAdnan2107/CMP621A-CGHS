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
    if SafeZoneDiscovered==True and TheWoodsDiscovered==True and TheVastDiscovered==True:
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

def FinalScene():
    print ("")
    print("The Master: You have defeated me, but you will never get the sword back.")
    SleepExtended()
    print(f"{MAINCHARACTER.Name}: You mean, the sword in my hands right now?")
    SleepExtended()
    print("The Master: What, HOW?")
    SleepExtended()
    print(f"{MAINCHARACTER.Name}: You will never get to know, Goodbye Master.")
    SleepExtended()
    print ("The Master vanishes from existance")
    SleepExtended()
    print ("You have defeated the Master, and have taken back the sword")
    SleepExtended()
    print ("You have saved the world from the Master's evil doings")
    SleepExtended()
    print ("You have won the game, Congratulations!")
    SleepExtended()
    print ("Thank you for playing The Master")
    SleepExtended()
    print ("Created by Ali Adnan")
    SleepExtended()
    print ("CMP621A - Andrew MacDougald")
    SleepExtended()
    print ("February 21st 2025")
    SleepExtended()
    print ("GAME OVER")
    exit()

def Fight(x):
    battle_over=False
    while not battle_over:
        print ("")
        print("1 - Talk")
        print("2 - Battle")
        print("3 - Flee")
        userinput = int(input("Select a choice: "))
        if userinput == 1:
            randint=random.randint(1, 3)
            if randint == 1:
                print("")
                print(f"{MAINCHARACTER.Name}: Hey, I'm {MAINCHARACTER.Name}, I'm just passing through")
                SleepExtended()
                print("FOE: I don't care who you are dude, my sole purpose is attacking you")
                SleepExtended()
                print(f"{MAINCHARACTER.Name}: Is there any way I can win you over?")
                SleepExtended()
                print("FOE: No, just no.")
                SleepExtended()
                print("")
            elif randint == 2:
                print("")
                print(f"{MAINCHARACTER.Name}: Totally not here to fight, just passing through")
                SleepExtended()
                print("FOE: Too bad, Come back here.")
                SleepExtended()
                print(f"{MAINCHARACTER.Name}: PLEASE I DONT WANT TO DEAL WITH THIS")
                SleepExtended()
                print("FOE: Like i said. TOO BAD.")
                SleepExtended()
                print("")
            elif randint == 3:
                print("")
                print(f"{MAINCHARACTER.Name}: No one can stop me in this journey")
                SleepExtended()
                print("FOE: You will regret saying that.")
                SleepExtended()
                print(f"{MAINCHARACTER.Name}: No regrets, Just courage.")
                SleepExtended()
                print("FOE: Could that statement be any cornier?")
                SleepExtended()
                print("")
        elif userinput == 2:
            while True:
                print("")
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
                SleepExtended()
                randint = random.randint(1, 2)
                if randint == 1:
                    print("You damaged the Foe.")
                    print("")
                    x.Health -= 40
                    x.Strength -= 10
                    print(f"You now have {MAINCHARACTER.Health} Health, the Foe has {x.Health} Health")
                    print("")
                    if x.Health <= 0:
                        print("You have defeated the Foe.")
                        battle_over=True
                        break
                elif randint ==2:
                    print("The Foe Hits you, Lost Health")
                    MAINCHARACTER.Health -= 10
                    MAINCHARACTER.XP -= 10
                    print(f"You now have {MAINCHARACTER.Health} Health, the Foe has {x.Health} Health")
                    print("")
                if MAINCHARACTER.Health <= 0:
                    print("You have been defeated by the Foe.")
                    print("GAME OVER")
                    exit()
                break  # Exit loop after battle
        elif userinput == 3:
            randint = random.randint(1, 2)
            if randint == 1:
                print("You have fled the foe")
                battle_over=True
                break
            elif randint == 2:
                print ("The Foe got to you, lost health and XP")
                MAINCHARACTER.Health -= 50
                MAINCHARACTER.XP -= 50
                print(f"You now have {MAINCHARACTER.Health} Health, and {MAINCHARACTER.XP} XP")
                print ("")
            if MAINCHARACTER.Health <= 0:
                print("You have been defeated by the Foe.")
                print("GAME OVER")
                exit()
            
            break  # Exit loop after fleeing
        else:
            print("Invalid choice, try again.")

def FinalFight(y):
    battle_over=False
    while not battle_over:
        print ("")
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
            y.Health -= 50
            y.Strength -= 20
            print(f"You now have {MAINCHARACTER.Health} Health, the Master has {y.Health} Health")
            print ("")
            if y.Health <= 0:
                print("You have defeated the Master.")
                battle_over=True
                FinalScene()
                break
        elif randint == 2:
            print("The Master hits you with a spell, you lose health and XP")
            MAINCHARACTER.Health -= 30
            MAINCHARACTER.XP -= 30
            print(f"You now have {MAINCHARACTER.Health} Health, the Master has {y.Health} Health")
            print ("")
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
        print ("")
        print("You are currently in the safe zone (South)")
        userinput = int(input("1 - Go West (Vast Dungeon)\n2- Go East (The Woods)\n3- Go North (The Hidden Dungeon)\nMake your Choice: "))
        if userinput == 1:
            TheVast()
            break
        elif userinput == 2:
            TheWoods()
            break
        elif userinput == 3:
            NorthUnlock()
            if statusunlocked==True:
                TheHiddenDungeon()
                break
            else:
                print("You have not unlocked this zone yet! Discover all areas to unlock")
        else:
            print("Invalid Input, Try again.")

def TravelFromHiddenDungeon():
    while True:
        print ("")
        print ("You are currently in the hidden dungeon (North)")
        userinput = input("1 - Go Forward (The Master's Lair) Y/N? : ")
        if userinput == "Y":
            TheMastersLair()
            break
        elif userinput == "N":
            SafeZone()
            break
        else:
            print("Invalid input, try again.")

def TravelFromTheWoods():
    while True:
        print ("")
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
        print ("")
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
    print("UNKNOWN: Oh, new guest! How's it going?")
    SleepExtended()
    print(f"{username}: Hey! I have no idea where I'm at? I'm {username}")
    SleepExtended()
    print("LLOYD: Hello, Welcome to my safe zone. I'm Lloyd, the owner of this place. Feel free to come by here to rest.")
    SleepExtended()

def SafeZone():
    global SafeZoneDiscovered
    SafeZoneDiscovered = True
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
                print ("")
                print ("Lloyd: You should go to the vast dungeon first, it's the closest to you and will teach you things.")
                print ("")
            elif ranint == 2:
                print ("")
                print ("Lloyd: You should go to the woods, Heard its a cool spot! but watch out...")
                print ("")
            elif ranint == 3:
                print ("")
                print ("Lloyd: The hidden dungeon, its a mysterious place. Some say its a myth. but The only way you can find out is by going")
                print ("")
        elif userinput == 2:
            TravelFromSafeZone()
            break
        elif userinput == 3:
            print ("")
            print (f"ALLOY: Hey {username}! You are currently in the Safe Zone, nothing can harm you. You can choose to rest here and brainstorm or you can continue your adventure")
            print ("")

def TheWoods():
    global TheWoodsDiscovered
    TheWoodsDiscovered = True
    print ("")
    print("You have entered the woods.")
    Sleep()
    print("You have encountered a foe.")
    Sleep()
    randomfoepick=random.randint(1,3)
    if randomfoepick==1:
        randomfoe=Foe1
    elif randomfoepick==2:
        randomfoe=Foe2
    elif randomfoepick==3:
        randomfoe=Foe3
    Fight(randomfoe)
    print ("")
    print("You continue to stroll through the woods. Nothing seems to be out of the ordinary.")
    SleepExtended()
    print("You have found a chest.")
    SleepExtended()
    print("You open the chest and find a letter.")
    SleepExtended()
    print("Letter reads, You will never find me, you will never get the sword back.")
    SleepExtended()
    print("The woods has been discovered")
    SleepExtended()
    TravelFromTheWoods()

def TheVast():
    global TheVastDiscovered
    TheVastDiscovered = True
    print ("")
    print("You have entered the vast dungeon.")
    Sleep()
    print("You have encountered a foe.")
    Sleep()
    print("The foe whispers to you...")
    Sleep()
    print("I know you, you will never get to the master. Quit while you can.")
    Sleep()
    randomfoepick=random.randint(1,3)
    if randomfoepick==1:
        randomfoe=Foe1
    elif randomfoepick==2:
        randomfoe=Foe2
    elif randomfoepick==3:
        randomfoe=Foe3
    Fight(randomfoe)
    print ("")
    print("You keep moving forward")
    Sleep()
    print ("The Dungeon is as vast as it can be, you keep moving forward and encounter another foe")
    Sleep()
    randomfoepick=random.randint(1,3)
    if randomfoepick==1:
        randomfoe=Foe1
    elif randomfoepick==2:
        randomfoe=Foe2
    elif randomfoepick==3:
        randomfoe=Foe3
    Fight(randomfoe)
    print ("")
    print("You find the last true key to the hidden dungeon")
    Sleep()
    print("You have discovered the vast dungeon")
    Sleep()
    TravelFromTheVast()

def TheHiddenDungeon():
    print ("")
    print("You have entered the hidden dungeon.")
    Sleep()
    print ("You lurk around to find whats so mysterious about this hidden dungeon.")
    Sleep()
    print("You have encountered a foe.")
    Sleep()
    randomfoepick=random.randint(1,3)
    if randomfoepick==1:
        randomfoe=Foe1
    elif randomfoepick==2:
        randomfoe=Foe2
    elif randomfoepick==3:
        randomfoe=Foe3
    Fight(randomfoe)
    print ("You keep moving forward and find a chest.")
    Sleep()
    print ("You open the chest and find a letter.")
    Sleep()
    print ("Letter reads, Leave my Lair while you still can... you will regret this")
    Sleep()
    TravelFromHiddenDungeon()

def TheMastersLair():
    print ("")
    print("You have entered the Master's Lair.")
    Sleep()
    print("You have encountered the Master.")
    Sleep()
    print("The Master: You have come to face me, I see.")
    SleepExtended()
    print(f"{MAINCHARACTER.Name}: I have come to take back what is mine.")
    SleepExtended()
    print("The Master: You will never get the sword back.")
    SleepExtended()
    print(f"{MAINCHARACTER.Name}: I will take it back, even if it means I have to fight you.")
    SleepExtended()
    print("The Master: You will regret this.")
    FinalFight(TheMaster)

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
print ("This is a text based game, you will be given choices to make and you will have to make the right choice to progress")
time.sleep(1)
print ("This game is also very random based, good luck!")
time.sleep(1)
Menu()
