import random

def shell_game() :

    shells = ['A','B','C']
    attempts = 2
    print("Welcome to Shell Game\n",
          "In this game, you must  guess which of the three shells (A, B, or C) hides the key.\n",
          "Each time, you'll have two attempts to find it.\n")
    print("You can choose the shell (A, B, or C) by typing either the letter corresponding.\n")

    for i in range(1,2) :
        good_shell = random.choice(shells)
        print("You have", attempts, "left\n")

        guess = input("Guess the shell that contains the key: ")

        guess_int = int(guess)
        if 97 <= guess_int <= 122:
            guess = chr(guess_int - 32)











