'''
Fort Boyard Simuator
Lubrano Lavaderci Camille / Sauvanet Ethan
This is the Pere Fouras challenge module.
This file is running the game chosen by the authors to be the Pere Fouras challenge.
Then returns a boolean indicating either the team wins or losses.
'''


import json
import random

#This is the load file function
#This function allows the riddles in the 'PFRiddles.json' to be implemented in this file
def load_riddles(file):
    with open(file, 'r') as f:
        riddles = json.load(f)
    return riddles

#this is the Pere Fouras Riddles function
#This function returns True or False in function of the result (if the team won or not)
def pere_fouras_riddles():
    #This imports the riddles to this function
    file = "./data/PFRiddles.json"
    riddles = load_riddles(file)
    riddle = random.choice(riddles)

    question = riddle['question']
    correct_answer = riddle['answer']
    attempts = 3

    print("You must answer the following riddle: ", question)

    #We have a while loop as the player has attempts until it goes to 0
    while attempts > 0:
        #puts both the guessed and correct answer in lower case to ensure no errors over whether the letters are upper or lower case
        answer_player = input('Enter your answer: ').lower()
        correct_answer = correct_answer.lower()

        if answer_player == correct_answer:
            print('\033[93mCongratulations, you win a key!\033[0m')
            return True
        else:
            #if the previous guess is incorrect the player will have one less attempt
            attempts -= 1
            if attempts > 0:
                print(f'Your answer is incorrect! You have {attempts} attempts left.')
            else:
                print("You have failed to answer the riddle! You do not win a key.")
                #if the player cannot find the correct answer after the three tries, the team loses
                return False

