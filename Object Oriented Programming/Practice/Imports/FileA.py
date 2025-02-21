import random


class randomnumgenerator:
    def __init__(self):
        self= 1
    def randomnumgen(self):
        print ("I am now randomly generating a number between 0 and 1, 10 times")
        for i in range(10):
            x=random.randint(0,1)
            print (f"{x} was generated")

x=0

randomnumgenerator.randomnumgen(x)
