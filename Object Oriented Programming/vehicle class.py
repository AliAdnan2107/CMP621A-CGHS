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
    def __del__(self):
        print("Vehicle Destructed")

Vehicles={
    1: Vehicle("Toyota", "Corolla", 2019, 20000),
    2: Vehicle("Honda", "Civic", 2018, 15000),
    3: Vehicle("Ford", "Fiesta", 2017, 10000),
    4: Vehicle("Nissan", "Sentra", 2025, 5000),
    5: Vehicle("Chevrolet", "Cruze", 2025, 2500)
}

def VehiclePrint():
    print("")
    print ("[Make, Model]")
    print("")
    for i in Vehicles:
        vehicle=Vehicles[i]
        print (i,":", vehicle.Make, vehicle.Model)
#Main

print ("Welcome to the Car Rental Indexing system")
print("")

while True:
    print ("")
    print ("1. Display all vehicles")
    print ("2. Select a Vehicle to View")
    print ("3. Update the mileage of a vehicle")
    print ("4. Add a new vehicle")
    print ("5. Remove a vehicle")
    print ("6. Quit Program")
    choice=int(input("Select a Menu Choice by number: "))
    if choice==1:
        print ("Here are the current index of vehicles")
        VehiclePrint()
    elif choice==2:
        print ("Select a vehicle to view")
        VehiclePrint()
        choice=int(input("Select a vehicle by number: "))
        vehicle=Vehicles[choice]
        print ("Make: ", vehicle.Make)
        print ("Model: ", vehicle.Model)
        print ("Year: ", vehicle.Year)
        print ("Mileage: ", vehicle.Mileage)
    elif choice==3:
        print ("Select a vehicle to update mileage")
        VehiclePrint()
        choice=int(input("Select a vehicle by number: "))
        vehicle=Vehicles[choice]
        mileage=int(input("Enter the new mileage: "))
        vehicle.Mileage=mileage
        print ("Mileage Updated")
        print ("Updated Information for Vehicle:")
        print ("Make: ", vehicle.Make)
        print ("Model: ", vehicle.Model)
        print ("Year: ", vehicle.Year)
        print ("Mileage: ", vehicle.Mileage)
    elif choice==4:
        print ("Enter the details of the new vehicle")
        make=input("Enter the make: ")
        model=input("Enter the model: ")
        year=int(input("Enter the year: "))
        mileage=int(input("Enter the mileage: "))
        Vehicles[len(Vehicles)+1]=Vehicle(make, model, year, mileage)
        print ("Vehicle Added")
    elif choice==5:
        print ("Select a vehicle to remove")
        VehiclePrint()
        choice=int(input("Select a vehicle by number: "))
        del Vehicles[choice]
        print ("Vehicle Removed")
    elif choice==6:
        print ("Thank you for using our software")
        break
    else:
        print ("Invalid input, Try again")
