from hangman_game import *
from guessing_game import *

""" Games Menu - Part 2 """

def choose_game():
    print("-"*20,"\nWelcome to the Menu!\n","-"*20)

    select_game = int(input("Select your Game\n(1) Guessing Game - (2) Hangman Game: "))


    if(select_game == 1):
        start_guessing()
    elif(select_game == 2):
        start_hangman()
    else: 
        while(select_game != 1 or select_game != 2):
            print('You have typed a wrong answer, try again!')
            select_game = int(input("Select your Game\n(1) Guessing Game - (2) Hangman Game: "))
            if(select_game == 1):
                start_guessing()
                break
            elif(select_game == 2):
                start_hangman()
                break

if (__name__ == '__main__'):
    choose_game()