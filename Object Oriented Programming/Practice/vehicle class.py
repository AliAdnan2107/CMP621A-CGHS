#Created by Ali Adnan
#7th of February 2025
#This program will create a class named Vehicle with a constructor and a destructor
#CMP621A

#Variables and Classes

class Vehicle: #Main Vehicle Class
    def __init__(self, Make, Model, Year, Mileage):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Mileage = Mileage
        print("Vehicle Constructed")

    def __del__(self):
        print(f"{self.Model} Destructed")


Vehicles=[   #Initial List of Vehicles
    Vehicle("Toyota", "Corolla", 2019, 20000),
    Vehicle("Honda", "Civic", 2018, 15000),
    Vehicle("Ford", "Fiesta", 2017, 10000),
    Vehicle("Nissan", "Sentra", 2025, 5000),
    Vehicle("Chevrolet", "Cruze", 2025, 2500),
    Vehicle("Ford","Mustang", 1964, 5000),
    Vehicle("Plymouth","Barracuda",1970,4000),
    Vehicle("Chevrolet", "Impala", 1965, 2000),
    Vehicle("Dodge","Charger",1968,45000)
]

def VehiclePrint(): #A function that will print the list of vehicles when needed
    print("")
    for index, i in enumerate(Vehicles, start=1):
        print (f"{index}. {i.Make} {i.Model}")

def ClassicVehiclePrint(): #A function that will print a list of classic vehicles when called
    print("")
    for i in Vehicles:
        if i.Year<=2005:
            print (f"{i.Make} {i.Model}")
        else:
            continue




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
    print ("6. Search Classic Vehicles")
    print ("7. Quit Program")
    choice=input("Select a Menu Choice by number: ")


#Display All Vehicles----------------------------------
    if choice=="1":
        print ("Here are the current index of vehicles")
        VehiclePrint()

#Select a Vehicle To View-----------------------------------
    elif choice=="2":
        print ("Select a vehicle to view")
        VehiclePrint()
        choice=input("Select a vehicle by number: ")
        if choice.isdigit(): #Failsafe
            choice=int(choice)
            vehicle=Vehicles[choice-1]
            print ("Make: ", vehicle.Make)
            print ("Model: ", vehicle.Model)
            print ("Year: ", vehicle.Year)
            print ("Mileage: ", vehicle.Mileage)
        else:
            print ("Invalid input, try again")
            continue

#Update Mileage of Vehicle------------------------------------
    elif choice=="3":
        print ("Select a vehicle to update mileage")
        VehiclePrint()
        choice=input("Select a vehicle by number: ")
        if choice.isdigit():
            choice=int(choice)
            vehicle=Vehicles[choice-1]
            mileage=input("Enter the new mileage: ")
            if mileage.isdigit():
                mileage=int(mileage)
                vehicle.Mileage=mileage
                print ("Mileage Updated")
                print ("Updated Information for Vehicle:")
                print ("Make: ", vehicle.Make)
                print ("Model: ", vehicle.Model)
                print ("Year: ", vehicle.Year)
                print ("Mileage: ", vehicle.Mileage)
            else:
                print("Invalid input, try again")
                continue
        else:
            print("Invalid input, try again")
            continue

#Add a new vehicle--------------------------------------------
    elif choice=="4":
        print ("Enter the details of the new vehicle")
        make=input("Enter the make: ")
        model=input("Enter the model: ")
        year=input("Enter the year: ")
        if year.isdigit():
            year=int(year)
        else:
            print ("Invalid input, Try Again")
            continue
        mileage=input("Enter the mileage: ")
        if mileage.isdigit():
            mileage=int(mileage)
        else:
            print ("Invalid input, try Again")
            continue
        if mileage==int(mileage) and year==int(year):
            newvehicle=Vehicle(make, model, year, mileage)
            Vehicles.append(newvehicle)
            print ("Vehicle Added")
            newvehicle=""

#Remove a vehicle----------------------------------------------
    elif choice=="5":
        print ("Select a vehicle to remove")
        VehiclePrint()
        choice=input("Select a vehicle by number: ")
        if choice.isdigit():
            choice=int(choice)
            del Vehicles[choice-1]
            print ("Vehicle Removed")
        else:
            print("Invalid input, Try Again")
            continue


#Find Classic Vehicles-----------------------------------------

    elif choice=="6":
        print ("Here is the current index of classic vehicles")
        ClassicVehiclePrint()

#Quit----------------------------------------------------------
    elif choice=="7":
        print ("Thank you for using our software")
        break

#Failsafe
    else:
        print ("Invalid input, Try again")
        continue