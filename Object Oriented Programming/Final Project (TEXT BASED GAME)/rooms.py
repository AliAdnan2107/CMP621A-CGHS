#Created by Ali Adnan
#CMP621A
#February 21st 2025
#PROJECT TEXT BASED GAME - ROOMS
from this import d
import time
import random
def Sleep():
    time.sleep(1)
def NorthUnlock():
    global statusunlocked
    statusunlocked=False
    if SafeZoneDiscovered==True and TheWoodsDiscovered==True and TheVastDiscovered==True:
        statusunlocked=True
    else:
        pass

def SafeZone():
    from scenes import username
    global SafeZoneDiscovered
    SafeZoneDiscovered=True
    Sleep()
    print ("UNKNOWN: Oh, new guest! How's it going?")
    Sleep()
    print (f"{username}: Hey! I have no idea where I'm at? I'm {username}")
    Sleep()
    print (f"LLOYD: Hello {username}, Welcome to my safezone. I'm Lloyd and you can always find me here for resources and help")
    Sleep()
    print ("LLOYD: How can I help you today?")
    SafeZoneShop=True
    Sleep()
    while SafeZoneShop==True:
        print ("1 - Acquire Resources")
        print ("2 - Ask For Advice")
        print ("3 - Leave to explore")
        print ("4 - Talk to Alloy")
        print ("5 - Back to Main Menu")
        userinput=int(input("Select a choice: "))
        if userinput==1:
            print ("LLOYD: What can I get you?")
            print ("1 - Additional Health")
            print ("2 - Additional Strength")
            print ("3 - Professional Advice")
            print ("4 - Tools")
            input1=int(input("Select a choice: "))
            if input1==1:
                "additional health"
            elif input1==2:
                "additional strength"
            elif input1==3:
                "professional advice"
            elif input1==4:
                "tools"
        elif userinput==2:
            randomnumgen=random.randint(1,3)
            if randomnumgen==1:
                print ("LLOYD: The woods will teach you alot, they are scary but they will teach you discipline. I say go explore!")
            elif randomnumgen==2:
                print ("LLOYD: Sometimes, you just need a break. Hangout here for as long as you would like!")
            elif randomnumgen==3:
                print ("LLOYD: Maybe order some of my professional advice, where I will give you confidential information about some of these zones! Check my store.")
        elif userinput==3:
            SafeZoneShop=False
            TravelFromSafeZone()
        elif userinput==4:
            print ("ALLOY: You are currently in the safezone, nothing can harm you here. Talk to Lloyd to purchase certain services and tools or go to explore the rest of the areas")

def TheWoods():
    from scenes import Foe1
    print ("You take a stroll through the woods, not thinking of much. Sounds of different creatures surround you")
    print ("What would you like to do?")
    print ("1 - Keep Exploring")
    print ("2 - Go Back to Safe Zone ")
    userinput=int(input("Select an option: "))
    if userinput==1:
        global TheWoodsDiscovered
        TheWoodsDiscovered=True
        print ()
    elif userinput==2:
        print ("You go back.")
        SafeZone()

def TheVast():
    from scenes import username
    global TheVastDiscovered
    TheVastDiscovered=True

def TheHiddenDungeon():
    from scenes import username

def TheMastersHut():
    "the masters hut"





def TravelFromSafeZone():
    print ("You are currently in the safe zone (West)")
    print ("1 - Go West (Vast Dungeon)")
    print ("2- Go East (The Woods)")
    print ("3- Go North (The Hidden Dungeon)")
    userinput=int(input("Make your Choice: "))
    if userinput==1:
        TheVast()
    if userinput==2:
        TheWoods()
    if userinput==3:
        if statusunlocked==True:
            TheHiddenDungeon()
        elif statusunlocked==False:
            print ("You have not unlocked this zone yet!, Discover all the other areas to unlock")
        