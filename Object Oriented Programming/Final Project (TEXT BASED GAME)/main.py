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
from initdialogue import *



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
   IntroScene()
    


#Main -----------------------------------------------------

print ("Ali Adnan Presents")
time.sleep(1)
print ("The Master")
time.sleep(1)
Menu()
