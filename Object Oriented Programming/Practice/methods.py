class CMP:
    def __init__(self,Name,Age,Grade):
        self.Name=Name
        self.Age=Age
        self.Grade=Grade
    
    def Print(self):
        print("The Name of the Student is", self.Name + ". The Age of the Student is", self.Age + ". The Grade of the Student is", self.Grade), 

Student1=CMP("Ali", "25", "A")
Student2=CMP("John", "22", "B")
Student3=CMP("Sara", "23", "C")
Student4=CMP("Mike", "24", "D")
Student5=CMP("Sara", "23", "C")
Student6=CMP("Anthony", "21", "A")
Student7=CMP("Noah", "29", "C")
Student8=CMP("James", "24", "D")

Student1.Print()
Student2.Print()
Student3.Print()
Student4.Print()
Student5.Print()
Student6.Print()
Student7.Print()
Student8.Print()