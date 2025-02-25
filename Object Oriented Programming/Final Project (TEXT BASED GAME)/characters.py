#Created by Ali Adnan
#CMP621A
#February 21st 2025
#PROJECT TEXT BASED GAME - CHARACTERS


class Characters:
    def __init__ (self, Name, Health, XP,):
        self.Name=Name
        self.Health=Health
        self.XP=XP

class Foe(Characters):
    def __init__(self, Name, Health, XP, EvilnessMeter):
        Characters.__init__(self, Name, Health, XP)
        self.EvilnessMeter=EvilnessMeter

    