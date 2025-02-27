#CREATED BY ALI ADNAN

import time
def SleepExtended():
    time.sleep(2.5)
def Sleep():
    time.sleep(1.5)
def IntroScene():
    print("")
    print ("UNKNOWN: You're awake")
    Sleep()
    print ("YOU: I am?")
    Sleep()
    print ("UNKNOWN: God I don't think you remember a thing")
    Sleep()
    print ("YOU: What happened?")
    Sleep()
    print ("UNKNOWN: He got to you...")
    Sleep()
    print ("YOU: Who Did?")
    Sleep()
    print ("UNKNOWN: The Master. He Betrayed you")
    Sleep()
    print ("YOU: Oh, He stole the sword aswell")
    Sleep()
    print ("UNKNOWN: THE Sword?")
    Sleep()
    print ("YOU: THE Sword.")
    Sleep()
    print ("UNKNOWN: What's your name partner?")
    global username
    username=input("Type in your name: ")
    print (f"{username}: The Name's {username}, and you are?")
    Sleep()
    print ("ALLOY: I'm alloy, I found you lying in the woods after you were betrayed I assume, Thought you were dead")
    Sleep()
    print (f"{username}: Well then, I suppose I can either continue to lie here")
    Sleep()
    print (f"{username}: Or Avenge myself.")
    Sleep()
    print ("-----------DIALOGUE END-----------")

def MidScene():
    print ("ALLOY: I will be your personal sidekick as you go through this journey.")
    Sleep()
    print ("ALLOY: Whenever you need advice, Select the number that corresponds with me")
    Sleep()
    print (f"ALLOY: Good Luck, {username}.")
    Sleep()
    print ("You start off in a shady but safe area, There are three directions you can proceed through")
    print("")
    Sleep()
    print ("North takes you to The Hidden Dungeon, the dungeon no one has dared to touch as it leads to the master's hut")
    print("")
    SleepExtended()
    print ("East takes you to The Woods, its dark and scary in there! But it will prepare you for what's to come")
    print("")
    SleepExtended()
    print ("West takes you to the Vast Dungeon, Slightly less scary than the woods but will also prepare you pretty well")
    print("")
    SleepExtended()
    print ("As you proceed through these areas, there will be Friends to guide you along the way or provide you with weapons, health etc.")
    print("")
    SleepExtended()
    

def Scene1():
    "scene 1"
