#Created By Ali Adnan
#CMP621A
#Review for variables and functions


#Variables-------------

y=0
GameScore=0

def GameScoreUp(y):
    global GameScore
    GameScore=y+1
    print ("Correct! Your Current score is " +str(GameScore))

def GameScoreDown(y):
    global GameScore
    y=GameScore
    print ("Incorrect! Your Current Score is " +str(GameScore))



#Main-------------
print ("Welcome to this game (python review cuz yes) \n")

while True:
    print ("Question 1 : Where is mars located?")
    print ("Option 1: Space ")
    print ("Option 2: Earth ")
    ans1=int(input("Select Option 1 or 2: "))
    if ans1==1:
        GameScoreUp(GameScore)
    elif ans1==2:
        GameScoreDown(GameScore)
    else:
        print ("Incorrect Input")
    print ("Question 2: How Old Are you?")
    print ("Option 1: Yes")
    print ("Option 2: No")
    ans2=int(input("Select Option 1 or 2: "))
    if ans2==1:
        GameScoreUp(GameScore)
    elif ans2==2:
        GameScoreDown(GameScore)
    else:
        print ("Incorrect input")
    print ("Your Final Score is " +str(GameScore))
    print ("Thank you for playing!")
    break

