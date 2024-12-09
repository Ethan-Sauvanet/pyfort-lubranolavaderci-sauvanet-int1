import random

def shell_game() :

    shells = ['A','B','C']
    attempts = 2
    print("Welcome to Shell Game\n" +
          "In this game, you must guess which of the three shells (A, B, or C) hides the key.\n" +
          "You have two attempts to find it.\n")
    print("You can choose the shell (A, B, or C) by typing the letter corresponding.\n")

    for i in range(attempts) :
        good_shell = random.choice(shells)
        print("You have", attempts, "attempts left")

        guess = input("Guess the shell that contains the key: ")

        guess_int = ord(guess)
        if 97 <= guess_int <= 122:
            guess = chr(guess_int - 32)

        if guess in shells :
            if guess == good_shell :
                print("You guessed the correct shell !\n")
                print("You obtain a key !\n")
                return True
            else :
                print("You guessed the wrong shell.\n")
        else :
            print("Your choice isn't in the listed shells.")
        attempts -= 1

    print("You lost, the key was under the shell :", good_shell)
    return False











