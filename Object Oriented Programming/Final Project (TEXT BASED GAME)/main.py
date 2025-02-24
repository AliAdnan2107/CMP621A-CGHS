#Created by Ali Adnan
#CMP621A
#February 21st 2025
#PROJECT TEXT BASED GAME


'''
TODO-
everything...
'''
#Imports
import time
from characters import *



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

def Sleep():
    time.sleep(2)

def Game():
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
    username=input("Type in your name: ")
    print (f"{username}: The Name's {username}, and you are?")
    print ("ALLOY: I'm alloy, I found you lying in the woods after you we're betrayed, Thought you were dead")



#Main -----------------------------------------------------

print ("Ali Adnan Presents")
time.sleep(1)
print ("The Master")
time.sleep(1)
Menu()
