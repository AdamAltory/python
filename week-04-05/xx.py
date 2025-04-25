import random
number = random.randint (1,10) 
while True:
    guess = int (input("guess the number (between 1 and 10):"))
    if guess < number:
        print("too low!")
    elif guess > number: 
        print("too high!")
    else: 
        print("you guessed it! the  number was ",  number)
        break