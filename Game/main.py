'''
This is the main program.
This program arranges all the different modules and files in order to create a realistic party of Fort Boyard.
For this, we need to import all the different modules to allow the program to work with them.
'''

from Game.utility_functions import*
from Game.math_challenges import*
from Game.logical_challenges import*
from Game.final_challenge import*
from Game.pere_fouras_challenge import*
from Game.chance_challenges import*


def game() :

    #Begining of the game
    introduction()
    compose_teams()

    number_keys = 0
    #The game itself is represented by a loop, the team plays until they gain 3 keys
    while number_keys < 3 :

        challenge = challenges_menu()
        if challenge == 1:
            math_challenge()
        if challenge == 2:
            battleship_game()
        if challenge == 3:
            chance_challenges()
        if challenge == 4:
            pere_fouras_riddles()

        if math_challenge() == True or battleship_game() == True or chance_challenges() == True or pere_fouras_riddles() == True :
            number_keys += 1
            print("You have", number_keys, "keys in totals.")
        else :
            print("You lost a challenge, pick another one. You need to have", 3-number_keys,"more key to access to the treasure room.")

    if number_keys == 3 :
        print("You have now enough keys to access the treasure room !")
        treasure_room()
    return

game()







