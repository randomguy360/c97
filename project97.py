import random
print ("Number guessing game")
num=random.randint(1,9)
chance=1

while(chance<=5):
    guess=int(input ("Guess the number"))
    if(num==guess):
        print("you won")
        break
    elif(num<guess):
        print("Guessed number is greater than the number...Try again")
    else:
        print("Guessed number is less than the number...Try again")
    chance=chance+1
if (chance>5):
    print("you lost")