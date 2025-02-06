class Player:
    def __init__(self, firstname,lastname, age, position,points):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.position=position
        self.points=points

    def print(self):
        print("The Player's Name is", self.firstname, self.lastname + ". The Player's Age is", self.age + ". The Player's Position is", self.position + ". The Player's Points are", self.points)

    
Players=[
    Player("Ali", "Adnan", "25", "Forward", "30"),
    Player("John", "Doe", "22", "Guard", "20"),
    Player("Sara", "Smith", "23", "Center", "15"),
    Player("Mike", "Johnson", "24", "Forward", "10"),
    Player("Sara", "Smith", "23", "Center", "15"),
    Player("Anthony", "Brown", "21", "Guard", "25"),
    Player("Noah", "Williams", "29", "Forward", "5"),
    Player("James", "Jones", "24", "Center", "10")
    ]


for player in Players:
    player.print()