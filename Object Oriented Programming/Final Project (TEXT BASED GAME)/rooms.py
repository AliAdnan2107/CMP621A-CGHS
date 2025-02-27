#Created by Ali Adnan
#CMP621A
#February 21st 2025
#PROJECT TEXT BASED GAME - ROOMS
import scenes
import characters
import main

def NorthUnlock():
    global statusunlocked
    statusunlocked=False
    if SafeZoneDiscovered=True and if TheWoodsDiscovered=True and if TheVastDiscovered=True:
def TravelFromSafeZone():
    print ("You are currently in the safe zone (West)")
    print ("1 - Go West (Vast Dungeon)")
    print ("2- Go East (The Woods)")
    print ("3- Go North (The Hidden Dungeon)")
    userinput=int(input("Make your Choice: "))
    if userinput==1:
        "west"
    if userinput==2:
        "east"
    if userinput==3:
        if statusunlocked==True:
            "north"
        elif statusunlocked==False:
            print ("You have not unlocked this zone yet!, Discover all the other areas to unlock")
        

def SafeZone():
    from scenes import username
    global SafeZoneDiscovered
    SafeZoneDiscovered=True
    print (f"LLOYD: Hello {username}, Welcome to my safezone. I'm Lloyd and you can always find me here for resources and help")
    print ("LLOYD: How can I help you today?")