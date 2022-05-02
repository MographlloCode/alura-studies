""" Hangman Game - Part 2 """

import random

def start_hangman():
    ''' Begin of Hangman Game '''

    opening_message()
    secret_word = load_secret_word()
    right_letters = init_right_letters(secret_word)

    print(right_letters)

    hanged = False
    right_answer = False
    errors = 0

    while(not hanged and not right_answer):

        tryout = ask_for_letter()
        if (tryout in secret_word):
            nice_try(tryout, right_letters, secret_word) 
        else:
            errors += 1
            draw_hang(errors)

        hanged = errors == 6
        right_answer = '_' not in right_letters
        
        if(right_answer):
            won_game(right_letters)
        elif(hanged):
            lost_game(errors, secret_word)
        
    print('End game.')

def opening_message():
    ''' Opening Message '''
    print("-"*30,"\nWelcome to the Hangman Game!\n","-"*30)

def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0,len(words))
    secret_word = words[number].lower()
    return secret_word

def init_right_letters(word):
    return ['_' for letter in word]

def ask_for_letter():
    return input('Type a letter: ').lower().strip()

def nice_try(tryout, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (tryout == letter):
            right_letters[index] = letter
            print(right_letters)
        index += 1

def lost_game(errors, secret_word):
    if(errors == 6):
        print("You died!")
        print(f"The word was {secret_word}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def won_game(right_letters):
    if ("_" not in right_letters):
        right_letters = str(right_letters)
        print(f'You will not be hanged! The word was {right_letters}')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")


    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")


    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")


    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")


    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")


    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
   

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")


    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == '__main__'):
    start_hangman()
