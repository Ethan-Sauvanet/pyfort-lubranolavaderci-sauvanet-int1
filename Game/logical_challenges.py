import random
import time

'''
Fort Boyard Simuator
Lubrano Lavaderci Camille / Sauvanet Ethan
This is the logical challenge module. 
This file is running the game chosen by the authors to be the logical challenge : Battleship game.
Then returns a boolean indicating either the team wins or losses.
'''

#This is the next player function.
#This function alternates between player 0 and player 1 and return its value (0 or 1).
#It takes as parameter the previous player in order to return the next one.
def next_player(player) :
    return 1 - player


#This is the empty grid function.
#This function generates an empty grid filled with spaces : " " and return this empty grid.
#This function takes no arguments because it don't need any external value to create an empty grid.
def empty_grid() :
    grid = [[0]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            grid[i][j] = " "
    return grid


#This is the display grid function.
#This function display a given grid with a given message to write above it.
#This function takes as parameter the grid and the message that we want to display.
def display_grid(grid,message) :
    print(message)
    #This will display the grid elements separated with "|"
    for i in range(3):
        for j in range(3):
            print("|", grid[i][j], end=" " + "| ")
        print("")
    print("_________________")
    return


#This is the ask position function.
#This function ask the user to enter some position in a certain typology and then return this position if it is valid, it also prevents any input errors.
#This function takes no argument because it don't need any to ask the user to enter a value.
def ask_position():
    while True:
        user_input = input("Enter a position of a boat in the format row,column: ")

        parts = user_input.split(",")
        #This condition prevent all possible input errors
        if len(parts) == 2 and len(parts[0]) == 1 and len(parts[1]) == 1 and ord('0') < ord(parts[0]) < ord('4') and ord('0') < ord(parts[1]) < ord('4') :
            row_str, column_str = parts[0].strip(), parts[1].strip()

            #Convert the values in Python (Python start with 0 when we start with 1)
            row = int(row_str) - 1
            column = int(column_str) - 1
            return (row, column)

        else:
            print("Invalid format. Please enter the position between 1 and 3 as : row,column (e.g.: 1,2).")


#This is the initialise function.
#This function allow the user to place his boats at beginning of the game and the return the grid of the player filled with his boats. For that it uses the empty grid and the ask position functions.
#This function takes no argument because the functions that it uses are called inside of it.
def initialise() :
    grid = empty_grid()
    display_grid(grid,"\nThis is your grid, fill it up by placing 2 boats (B) :")

    #Ensure that the 2 boats are not placed in the same slot
    position1 = ask_position()
    position2 = position1
    while position1 == position2:
        position2 = ask_position()

    #Fill the grid with the positions given by the user
    a, b, c, d = position1[0], position1[1], position2[0], position2[1]

    grid[a][b] = 'B'
    grid[c][d] = 'B'

    display_grid(grid, "\nThis is your grid filled with your boats :")
    return grid


#This is the turn function.
#This function is running a turn in the battleship game. During this turn the player will have to enter positions (via the ask position function) in order to shoot the opponent's grid.
#This function takes as argument the player, his previous shots, and the opponent's grid in order to verify if the shot sink or not the opponent's boats and then store the position of the shot.
def turn(player, player_shots_grid, opponent_grid) :
    #Verify if it is the player or the game master playing
    if player == 0 :
        display_grid(player_shots_grid,"\nThis is your previous shots :")

        #If this is the player, ask the player some positions to shoot at
        print("It's your time to shoot !")
        attack = ask_position()
        e, f = attack[0], attack[1]

    #If it is the game master's turn, the positions of the shoot are chosen randomly
    else :
        print("The game master is shooting...")
        time.sleep(2)
        e = random.randint(0,2)
        f = random.randint(0,2)

    #This loop ensure that any player does not shoot twice on the same spot
    while player_shots_grid[e][f] == '.' or player_shots_grid[e][f] == 'X':
        if player == 0 :
            print("You have already shot at this position Enter another position.")
            attack = ask_position()
            e, f = attack[0], attack[1]
        else :
            e = random.randint(0,2)
            f = random.randint(0,2)

    #Verify if there is a boat or not at this position
    if opponent_grid[e][f] == 'B':
        print("\033[92mHit, sunk !\033[0m")
        player_shots_grid[e][f] = 'X'
        time.sleep(1)
    else :
        print("\033[91mSplash...\033[0m")
        player_shots_grid[e][f] = '.'
        time.sleep(1)
    return


#This is the has won function.
#This function is verifying if any player won or not the Battleship game by looking at his shots grid. It returns True or False depending on the winner.
#In order to look at the current player shots grid, the function need as parameter the player shots grid.
def has_won(player_shots_grid) :
    count = 0
    #Verifying in all the shots grid
    for i in range(3):
        for j in range(3):
            if player_shots_grid[i][j] == 'X':
                count += 1
    #If 2 boats are sunk, the player wins
    if count == 2 :
        return True
    else :
        return False


#This is the Battleship game program.
#It is the main program that arranges all the functions above in a game.
#It takes no arguments because all the functions are called inside.
def battleship_game() :

    print("Welcome to Battleship game!")
    print("In this game, your goal is to sink all the opponent's ships.")
    print("First you have to place your boats, then turn by turn you'll shoot the opponent's grid until you sink all his boats.")
    print("Let the game begin !")

    grid = initialise()

    #It fills the game master grid with 2 boats placed randomly
    print("The game Master is placing his boats...")
    grid_master = empty_grid()
    a,b,c,d = random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)
    while c == a and d == b :
        c, d = random.randint(0, 2), random.randint(0, 2)
    grid_master[a][b], grid_master[c][d] = 'B', 'B'
    time.sleep(3)

    player_grid_shots = empty_grid()
    master_shots_grid = empty_grid()

    #The loop simulates the game, it stops when a player have sunk all of it's opponent's boats.
    player = 1
    while has_won(player_grid_shots) == False and has_won(master_shots_grid) == False :

        player = next_player(player)
        if player == 0 :
            turn(player, player_grid_shots, grid_master)
            has_won(player_grid_shots)

        else :
            turn(player, master_shots_grid, grid)
            has_won(master_shots_grid)

    #Verifying if either the player or the game master won or not the game
    if has_won(player_grid_shots) :
        print("You win!")
        print("\033[93mYou obtain a key\033[0m")
        return True

    if has_won(master_shots_grid) :
        print("The game master win!")
        return False


