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
    def tell(self):
        print ("Name: ", self.Name )
        print ("Health: ", self.Health)
        print ("Strength: ", self.Strength) 


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
    def __str__(self):
        return f"Your Character currently has {self.XP} XP, When you increase your XP you increase your other attributes"
