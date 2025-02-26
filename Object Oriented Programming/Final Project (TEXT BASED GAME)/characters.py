#Created by Ali Adnan
#CMP621A
#February 21st 2025
#PROJECT TEXT BASED GAME - CHARACTERS

from initdialogue import *


class Characters:
    def __init__ (self, Name, Health, Strength,):
        self.Name=Name
        self.Health=Health
        self.Strength=Strength

class Foe(Characters):
    def __init__(self, Name, Health, Strength, EvilnessMeter):
        Characters.__init__(self, Name, Health, Strength)
        self.EvilnessMeter=EvilnessMeter

class Friend(Characters):
    def __init__(self, Name, Health, Strength, FriendshipMeter):
        Characters.__init__(self, Name, Health, Strength)
        self.FriendshipMeter=FriendshipMeter

class MainCharacters(Characters):
    def __init__(self, Name, Health, Strength, XP ):
        Characters.__init__(self, Name, Health, Strength)
        self.XP=XP



def BuildPick():
    print ("Select your initial build: ")
    print ("1 - 150 Health, 60 Strength, 20XP")
    print ("2 - 100 Health, 80 Strength, 40XP")
    print ("3 - 80 Health, 120 Strength, 30XP")
