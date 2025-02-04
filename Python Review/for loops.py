num= int(input ("Pick a number: "))
numinp=num

while num>0:
    n=num-1
    print (n)
    num=n

if num==0:
    print ("You picked a value of " +str(numinp) +" Which completed a countdown to 0")