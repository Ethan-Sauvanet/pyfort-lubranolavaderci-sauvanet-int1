import json
import random

def load_riddles(file="PFRiddles.json"):
    with open(file, 'r') as f:
        riddles = json.load(f)
    return riddles

def pere_fouras_riddles():
    riddles = load_riddles()
    riddle = random.choice(riddles)

    question = riddle['question']
    correct_answer = riddle['answer']
    attempts = 3

    print("You must answer the following riddle : ", question)

    while attempts > 0:
        answer_player = input('Enter your answer : ').lower()
        correct_answer = correct_answer.lower()

        if answer_player == correct_answer:
            print('\033[93mCongratulations, you win a key !\033[0m')
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print('Your answer is incorrect! You have ', attempts, ' left.')
            else:
                print("You have failed to answer the riddle! You do not win a key")
                return False
