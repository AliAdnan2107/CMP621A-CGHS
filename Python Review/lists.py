namelist=[]
print ("Welcome to the name directory")
CompanyName=input("Please register your company name: ")
print ("Your Company Name has been successfully registered as " +CompanyName )
print ("Your Name list currently has", len(namelist), "Employees Registered")
while True:
    names=input("Please register an employee name, once Done type done: ")
    if names=="Done":
        print ("Your Name list currently has", len(namelist), "Employees Registered")
        print (namelist)
        print ("Thank you for using my software")
        break
    else:
        namelist.append(names)

