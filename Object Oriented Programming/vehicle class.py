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

Vehicles=[
    Vehicle("Toyota", "Corolla", 2019, 20000),
    Vehicle("Honda", "Civic", 2018, 15000),
    Vehicle("Ford", "Fiesta", 2017, 10000),
    Vehicle("Nissan", "Sentra", 2025, 5000),
    Vehicle("Chevrolet", "Cruze", 2025, 2500)
]

def VehiclePrint():
    print("")
    for index, i in enumerate(Vehicles, start=1):
        print (f"{index}. {i.Make} {i.Model}")



#Main---------------------------------------

print ("Welcome to the Car Rental Indexing system")
print("")

#Program Loop-------------------------------
while True:
    print ("")
    print ("1. Display all vehicles")
    print ("2. Select a Vehicle to View")
    print ("3. Update the mileage of a vehicle")
    print ("4. Add a new vehicle")
    print ("5. Remove a vehicle")
    print ("6. Quit Program")
    choice=input("Select a Menu Choice by number: ")


#Display All Vehicles----------------------------------
    if choice=="1":
        print ("Here are the current index of vehicles")
        VehiclePrint()

#Select a Vehicle To View-----------------------------------
    elif choice=="2":
        print ("Select a vehicle to view")
        VehiclePrint()
        choice=int(input("Select a vehicle by number: "))
        vehicle=Vehicles[choice-1]
        print ("Make: ", vehicle.Make)
        print ("Model: ", vehicle.Model)
        print ("Year: ", vehicle.Year)
        print ("Mileage: ", vehicle.Mileage)

#Update Mileage of Vehicle------------------------------------
    elif choice=="3":
        print ("Select a vehicle to update mileage")
        VehiclePrint()
        choice=int(input("Select a vehicle by number: "))
        vehicle=Vehicles[choice-1]
        mileage=int(input("Enter the new mileage: "))
        vehicle.Mileage=mileage
        print ("Mileage Updated")
        print ("Updated Information for Vehicle:")
        print ("Make: ", vehicle.Make)
        print ("Model: ", vehicle.Model)
        print ("Year: ", vehicle.Year)
        print ("Mileage: ", vehicle.Mileage)

#Add a new vehicle--------------------------------------------
    elif choice=="4":
        print ("Enter the details of the new vehicle")
        make=input("Enter the make: ")
        model=input("Enter the model: ")
        year=int(input("Enter the year: "))
        mileage=int(input("Enter the mileage: "))
        newvehicle=Vehicle(make, model, year, mileage)
        Vehicles.append(newvehicle)
        print ("Vehicle Added")

#Remove a vehicle----------------------------------------------
    elif choice=="5":
        print ("Select a vehicle to remove")
        VehiclePrint()
        choice=int(input("Select a vehicle by number: "))
        del Vehicles[choice-1]
        print ("Vehicle Removed")

#Quit----------------------------------------------------------
    elif choice=="6":
        print ("Thank you for using our software")
        break

#Failsafe
    else:
        print ("Invalid input, Try again")
