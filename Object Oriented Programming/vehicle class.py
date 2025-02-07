#Created by Ali Adnan
#7th of February 2025
#This program will create a class named Vehicle with a constructor and a destructor
#CMP621A

#Variables and Classes

class Vehicle:
    def __init__(self, Make, Model, Year, Mileage):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Mileage = Mileage
        print("Vehicle Constructed")
    def printv(self):
        print(self.Make, self.Model, self.Year, self.Mileage)
    def __del__(self):
        print("Vehicle Destructed")

Vehicles={
    1: Vehicle("Toyota", "Corolla", 2019, 20000),
    2: Vehicle("Honda", "Civic", 2018, 15000),
    3: Vehicle("Ford", "Fiesta", 2017, 10000),
    4: Vehicle("Nissan", "Sentra", 2025, 5000),
    5: Vehicle("Chevrolet", "Cruze", 2025, 2500)
}

#Main

print ("Welcome to the Car Rental Indexing system")

while True:
    print ("1. Display all vehicles")
    print ("2. Select a Vehicle to View")
    print ("3. Update the mileage of a vehicle")
    print ("4. Add a new vehicle")
    print ("5. Remove a vehicle")
    print ("6. Quit Program")
    choice=int(input("Select a Menu Choice by number: "))
    if choice==1:
        print ("Here are the current index of vehicles")
        print ("[Make, Model, Year, Mileage]")
        for key, row in Vehicles.items():
            print(row.Make, row.Model, row.Year, row.Mileage)
    elif choice==2:
        "part2"
    elif choice==3:
        "part3"
    elif choice==4:
        "part4"
    elif choice==5:
        "part 5"
    elif choice==6:
        "part 6"
    else:
        print ("Invalid input, Try again")
