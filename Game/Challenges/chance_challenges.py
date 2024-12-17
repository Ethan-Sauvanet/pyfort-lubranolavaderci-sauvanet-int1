import random

def chance_challenges() :
    challenges = [shell_game, roll_dice_game]
    challenge = random.choice(challenges)
    return challenge()

def shell_game() :

    shells = ['A','B','C']
    attempts = 2
    print("Welcome to Shell Game !\n" +
          "In this game, you must guess which of the three shells (A, B, or C) hides the key.\n" +
          "You have two attempts to find it.\n")
    print("You can choose the shell (A, B, or C) by typing the letter corresponding.\n")

    for i in range(attempts) :
        good_shell = random.choice(shells)
        print("You have", attempts, "attempts left")

        print("The Master hides the key,")
        print(" ---    ---    ---")
        print("| A |  | B |  | C |")
        print(" ---    ---    ---")
        guess = input("Guess the shell that contains the key : ")

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


def roll_dice_game() :

    print("Welcome to Roll Dice Game !\n" +
    "In this game, the game master and you have 3 attempts to roll two dices.\n" +
    "The first one to do a 6 with one of his dices win the game !\n")

    attempts = 3

    for i in range(attempts) :
        print("You have", attempts - i, "attempts left.")

        enter_key = input("Press ENTER to roll the dice : ")
        while enter_key != "" :
            print("You have entered the wrong key.")
            enter_key = input("Press ENTER to roll the dice : ")

        rolls = (random.randint(1,6), random.randint(1,6))
        print("\nYour rolls : [",rolls[0],"] and [",rolls[1],"]")

        for item in rolls :
            if item == 6 :
                print("You rolled 6 ! You win the game!\n" +
                      "The key is yours, you can continue.")
                return True
        print("You didn't roll a 6. Game master's turn !")

        master_rolls = (random.randint(1, 6), random.randint(1, 6))
        print("\nMaster rolls : [", master_rolls[0], "] and [", master_rolls[1], "]")

        for item in master_rolls :
            if item == 6 :
                print("The Master rolled a 6 ! You lost the game!\n")
                return False
        print("Neither player rolled a 6. The game continue !\n")

    print("No player has scored a 6 after 3 tries. It's a draw !\n")
    return False

chance_challenges()















