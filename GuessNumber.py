import random
randomNumber = random.randrange(0,20)
print("Random number between 0 and 20 has been generated")
guessed = False
while guessed==False:
    userNumber = int(input("Take a guess: "))
    if userNumber==randomNumber:
        guessed = True
        print("Excellent, Well done!")
    elif userNumber>randomNumber:
        print("Try one more time, a bit lower")
    elif userNumber < randomNumber:
        print("Try one more time, a bit higher")
print("Yes, you can!")
