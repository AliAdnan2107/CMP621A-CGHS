class Player:
    def __init__(self, firstname,lastname, age, position,points):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.position=position
        self.points=points

    def print(self):
        print("The Player's Name is", self.firstname, self.lastname + ". The Player's Age is", self.age + ". The Player's Position is", self.position + ". The Player's Points are", self.points)



players = [Player("Lebron", "James", 35, "Point Guard", 30), Player("Kevin", "Durant", 32, "Small Forward", 25), Player("Kawhi", "Leonard", 29, "Shooting Guard", 20)]

for player in players:
    player.print()

    """
    sammy constructed
    sammy count 1
    sammy count 2
    jenny constructed
    jenny count 1
    80
    """