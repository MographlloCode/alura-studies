""" Guessing Game - Lesson 2/3/4/5/6/7/8 - Part 1 """

import random

def start_guessing():
    ''' Begin of Guessing Game '''
    print("-"*30,"\nWelcome to the Guessing Game!\n","-"*30)

    # Variables
    secret_number = random.randrange(1,101) # Using random library to generate a random number
    print(secret_number)
    tryouts = 0
    points = 1000

    # Game w/ While

    print("Choose the difficulty level")
    level = int(input("(1) Easy - (2) Medium - (3) Hard\nChoose your level: "))

    if(level == 1):
        tryouts = 10
    elif(level == 2):
        tryouts = 5
    elif(level == 3):
        tryouts = 3

    while(tryouts):
        guess = int(input("Type your guess: ")) # Using int() before the input turns the type of "input" from string to int

        right_guess = secret_number == guess
        higher_guess = guess > secret_number
        lower_guess = guess < secret_number

        if(right_guess):
            print(f"Congratulations! The secret number is {guess}!") # the "f" is used to format the string and leting it be 
                                                                    # able to receive the variable inside the sentence, using {variable}
            tryouts = 0
        else:
            if(higher_guess):
                print("You guessed a higher number than the secret number.")
                points -= 100
                tryouts -= 1
            elif(lower_guess):
                print("You guessed a lower number than the secret number.")
                points -= 100
                tryouts -= 1

if (__name__ == '__main__'):
    start_guessing()

# Game w/ For
# for round in range(1, tryouts + 1):
#     guess = int(input("Type your guess: ")) # Using int() before the input turns the type of "input" from string to int

#     right_guess = secret_number == guess
#     higher_guess = guess > secret_number
#     lower_guess = guess < secret_number

#     if(right_guess):
#         print(f"Congratulations! The secret number is {guess}!") # the "f" is used to format the string and leting it be                                                       # able to receive the variable inside the sentence, using {variable}
#         break
#     elif(higher_guess):
#         print("You guessed a higher number than the secret number.")
#     elif(lower_guess):
#         print("You guessed a lower number than the secret number.")