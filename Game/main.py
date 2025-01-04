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







