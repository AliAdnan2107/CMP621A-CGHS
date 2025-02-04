#Created by Ali Adnan
#CMP621A
#This is a review of python, If user guesses number program responds
#2nd of February 2025

print ("Welcome to my program\n")
guess= int(input ("Pick a number between one and twelve: "))

if guess >=6 and guess<=12:
    print ("You guessed a number larger than 6!, your guess was " + str(guess))
elif guess <6 and guess >0:
    print ("You guessed a number lower than 6! Your guess was " +str(guess))
else:
    print ("Something looks wrong!")
