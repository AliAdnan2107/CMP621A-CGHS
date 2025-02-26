#Created by Ali Adnan
#CMP621A
#February 21st 2025
#PROJECT TEXT BASED GAME - CHARACTERS

from tokenize import Name

class Characters:
    def __init__ (self, Name, Health, Strength,):
        self.Name=Name
        self.Health=Health
        self.Strength=Strength
    def __str__(self):
        return ("Name: ", self.Name )("Health: ", self.Health)("Strength: ", self.Strength) ("XP : ", self.XP)


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



