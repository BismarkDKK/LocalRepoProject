# A program to make a user guess the number of the computer

import random


secret_number = random.randint(1,10)

user_number = int(input("""I'm thinking of a number between 1 and 10. Can you" 
                            guess it? """))

#print(secret_number)
match user_number:
    case secret_number:
        print("Congratulations, you guessed it!")
    case _:
        if user_number > secret_number:
            print("Nope, your guess is a bit high. Give it another shot!")
        else:
            print("Nope, your guess is a bit low. Give it another shot!")
