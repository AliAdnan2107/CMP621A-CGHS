class Pet:
    def __init__(self, age, gender, breed, animal):
        self.animal=animal
        self.breed=breed
        self.age=age
        self.gender=gender


p1=Pet("6 Years old","Male","Serbian","Cat")
p2=Pet("2 Years old","Female","Golden Retriever","Dog")

print ("The age of pet 1 is", p1.age)
print ("The Breed of pet 2 is", p2.breed)

