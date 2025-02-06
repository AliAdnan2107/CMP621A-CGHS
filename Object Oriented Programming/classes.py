#Created by Ali Adnan
#2/6/2025


#Variables

class Pet:
    Breed=""
    Animal=""
    Age=""
    Gender=""

Pet1=Pet()
Pet1.Breed="Chiwawa"
Pet1.Age="5"
Pet1.Gender="Male"
Pet1.Animal="Dog"

Pet2=Pet()
Pet2.Breed="Serbian"
Pet2.Age="7"
Pet2.Gender="Female"
Pet2.Animal="Cat"

print ("The Animal is a", Pet1.Animal, "It's", Pet1.Age, "Years Old.", Pet1.Gender, "And it is a", Pet1.Breed)
print ("The Animal is a", Pet2.Animal, "It's", Pet2.Age, "Years Old.", Pet2.Gender, "And it is a", Pet2.Breed)


print ("A unique animal would be", Pet2.Animal, "With the Age being", Pet1.Age, "The gender being", Pet2.Gender, "And the breed being", Pet1.Breed)
