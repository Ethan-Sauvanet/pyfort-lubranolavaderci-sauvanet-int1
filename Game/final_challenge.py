import json
import random

def treasure_room():

    attempts = 3
    answer_correct = False

    with open('Data/TRClues.json', 'r') as file:
        tv_game = json.load(file)

    tv_shows = list(tv_game.keys())
    tv_show = tv_shows[0]

    years = list(tv_game[tv_show].keys())
    year = random.choice(years)

    shows = list(tv_game[tv_show][year].keys())
    show = random.choice(shows)

    clues = tv_game[tv_show][year][show]["Clues"]
    code_word = tv_game[tv_show][year][show]["CODE-WORD"]

    print("Here are your clues : ")
    for clue in clues[:3]:
        print(f"- {clue}")
    print("")
    while attempts > 0:

        guess = input("Enter your guess for the code word : ").strip()

        if guess.lower() == code_word.lower():
            answer_correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong ! You have {attempts} attempts left.")

                if 3 + (3 - attempts) < len(clues):
                    print(f"Here is an additional clue: {clues[3 + (3 - attempts)]}\n")
            else:
                print(f"Sorry, there is no attempts remaining, you failed. The correct code word was: {code_word}.")

    if answer_correct:
        print("\033[93mCongratulations ! You guessed the correct code word and accessed the treasure room !\033[0m")
    else:
        print("Better luck next time !")
