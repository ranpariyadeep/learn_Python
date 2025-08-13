import random

randNum = random.randint(1, 100)
print("Welcome to the Guess The Number Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")



def guess_the_number():
 
 guess = int(input("Enter your guess: "))

 if(guess == randNum):
    print("Congratulations! You guessed the number correctly." )
    return
 else:
    if(guess < randNum):
        print("Your guess is too low.")
      
        guess_the_number()
    else:
        print("Your guess is too high." ) 
        
        guess_the_number()  


guess_the_number()
print("Thanks for playing!")        