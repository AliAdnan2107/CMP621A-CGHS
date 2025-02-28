#Created by Ali Adnan
#CMP621A
#February 21st 2025
#PROJECT TEXT BASED GAME


'''
TODO-
-Create Side Characters in character.py
-Plot and Create "Rooms"
-Implement Failsafes
'''

#Imports ------------------------------------------------
import time
from characters import *
from scenes import *
from rooms import *



#Classes / Variables -------------------------------------

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

def BuildPick():
    from scenes import username
    print ("Select your initial build: ")
    print ("1 - 150 Health, 60 Strength, 20XP")
    print ("2 - 100 Health, 80 Strength, 40XP")
    print ("3 - 80 Health, 120 Strength, 30XP")
    buildinput=int(input("Pick a number: "))
    if buildinput==1:
        MAINCHARACTER=MainCharacters(username, 150, 60, 20)
        print (f"Your Character {MAINCHARACTER.Name} has been built with these features")
        MAINCHARACTER.tell()
        print (MAINCHARACTER)
        print ("")
    elif buildinput==2:
        MAINCHARACTER=MainCharacters(username, 100, 80, 40)
        print (f"Your Character {MAINCHARACTER.Name} has been built with these features")
        MAINCHARACTER.tell()
        print (MAINCHARACTER)
        print ("")
    elif buildinput==3:
        MAINCHARACTER=MainCharacters(username, 80, 120, 30)
        print (f"Your Character {MAINCHARACTER.Name} has been built with these features")
        MAINCHARACTER.tell()
        print (MAINCHARACTER)
        print ("")
    else:
        "failsafe"



def Game():
   IntroScene()
   BuildPick()
   MidScene()
   userinput=input("Ready to start? (Y/N) : ")
   if userinput=="Y":
       pass
   elif userinput=="N":
       quitinput=input("This will return you to main menu, Confirm? (Y/N) : ")
       if quitinput=="Y":
           Menu()
       elif quitinput=="N":
            pass
   Scene1()
    
    


#Main -----------------------------------------------------

print ("Ali Adnan Presents")
time.sleep(1)
print ("The Master")
time.sleep(1)
Menu()
