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
    global game_playing
    introduction()
    team = compose_teams()

    number_keys = 0
    #The game itself is represented by a loop, the team plays until they gain 3 keys
    while number_keys < 3 :

        challenge = challenges_menu()

        choose_player(team)
        if challenge == 1:
            game_playing = math_challenge()
        if challenge == 2:
            game_playing = battleship_game()
        if challenge == 3:
            game_playing = chance_challenges()
        if challenge == 4:
            game_playing = pere_fouras_riddles()

        if game_playing :
            number_keys += 1
            print("\nYou have", number_keys, "keys in total.", 3-number_keys,"left !")
        else :
            print("\nYou lost a game.", 3-number_keys,"more key are needed to access the treasure room.")

    if number_keys == 3 :
        print("You have now enough keys to access the treasure room !\n")
        treasure_room()
    return

game()







