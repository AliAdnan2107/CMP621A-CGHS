#Created by Ali Adnan
#CMP621A
#February 20th 2025
#This program demonstrates 3 private attributes that include a setter and getter

#Classes and variables-------------------

class Citizen:

    def __init__(self, Name, DOB, Residence,SIN):
        self.__Name=Name
        self.__DOB=DOB
        self.__Residence=Residence
        self.__SIN=SIN

    def get_name(self):
        return self.__Name

    def get_DOB(self):
        return self.__DOB

    def get_residence(self):
        return self.__Residence    
    
    @classmethod
    def get_SIN(sin_class, SIN):
        return sin_class(SIN)
    @classmethod
    def set_SIN(sin_class,SIN):
        sin_class=SIN
        return sin_class(SIN)





#Main------------------------------------


citizen1=Citizen("Ali","March 21st","Charlottetown","1234567")
print(citizen1.get_name())
print(citizen1.get_DOB())
print(citizen1.get_residence())

citizen1.set_SIN("123456789")
print (citizen1.get_SIN)