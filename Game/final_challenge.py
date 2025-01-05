import json
import random

'''
Fort Boyard Simuator
Lubrano Lavaderci Camille / Sauvanet Ethan
This is the final challenge module. 
This file runs the treasure room program which is the final challenge of the adventure.
'''

#This is the treasure room program.
#This program is giving the team few clues to find a code word. Once this code word found, the team can access to the treasure room and win the game !
#It doesn't require any arguments because this program is working with a file which needs to be opened in the program itself.
def treasure_room():

    attempts = 3
    answer_correct = False

    #Opening the file that contains all the data
    with open('Data/TRClues.json', 'r') as file:
        tv_game = json.load(file)

    #Randomly choosing a word code and the relative clues
    tv_shows = list(tv_game.keys())
    tv_show = tv_shows[0]

    years = list(tv_game[tv_show].keys())
    year = random.choice(years)

    shows = list(tv_game[tv_show][year].keys())
    show = random.choice(shows)

    clues = tv_game[tv_show][year][show]["Clues"]
    code_word = tv_game[tv_show][year][show]["CODE-WORD"]

    print("You finally reached the treasure room ! Now you must decipher the code needed to open the door and access the treasure.")
    #Displaying the clues
    print("Here are your clues : ")
    for clue in clues[:3]:
        print(f"- {clue}")
    print("")

    #The loop is simulating the player attempts to find the code word
    while attempts > 0:

        guess = input("Enter your guess for the code word : ").strip()

        #As we can't use .lower(), i created a loop that compares letter by letter even if some are in caps or not
        if len(guess) == len(code_word):
            answer_correct = True
            for i in range(len(guess)):
                g = guess[i]
                c = code_word[i]
                if not (g == c or (ord('A') <= ord(g) <= ord('Z') and ord(g) + 32 == ord(c)) or
                        (ord('a') <= ord(g) <= ord('z') and ord(g) - 32 == ord(c))):
                    answer_correct = False
                    break
            if answer_correct:
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
        print("\033[93mCongratulations ! You guessed the correct code word and accessed the treasure room ! You won !\033[0m")
    else:
        print("Better luck next time !")
    return
