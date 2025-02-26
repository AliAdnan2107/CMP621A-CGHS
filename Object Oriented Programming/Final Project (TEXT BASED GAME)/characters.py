#Created by Ali Adnan
#CMP621A
#February 21st 2025
#PROJECT TEXT BASED GAME - CHARACTERS


class Characters:
    def __init__ (self, Name, Health, Strength,):
        self.Name=Name
        self.Health=Health
        self.Strength=Strength

class Foe(Characters):
    def __init__(self, Name, Health, Strength, EvilnessMeter):
        Characters.__init__(self, Name, Health, Strength)
        self.EvilnessMeter=EvilnessMeter

class MainCharacters(Characters):
    def __init__(self, Name, Health, Strength, XP ):
        Characters.__init__(self, Name, Health, Strength)
        self.XP=XP