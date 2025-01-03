import random
import time

def next_player(player) :
    return 1 - player

def empty_grid() :
    grid = [[0]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            grid[i][j] = " "
    return grid

def display_grid(grid,message) :
    print(message)
    for i in range(3):
        for j in range(3):
            print("|", grid[i][j], end=" " + "| ")
        print("")
    print("_________________")
    return

def ask_position():
    while True:
        user_input = input("Enter a position of a boat in the format row,column: ")

        parts = user_input.split(",")
        if len(parts) == 2 and len(parts[0]) == 1 and len(parts[1]) == 1 and ord('0') < ord(parts[0]) <= ord(parts[1]) < ord('4') :
            row_str, column_str = parts[0].strip(), parts[1].strip()

            row = int(row_str) - 1
            column = int(column_str) - 1
            return (row, column)

        else:
            print("Invalid format. Please enter the position between 1 and 3 as : row,column (e.g.: 1,2).")

def initialise() :
    grid = empty_grid()
    display_grid(grid,"\nThis is your grid, fill it up by placing 2 boats (B) :")

    position1 = ask_position()
    position2 = position1
    while position1 == position2:
        position2 = ask_position()

    a, b, c, d = position1[0], position1[1], position2[0], position2[1]

    grid[a][b] = 'B'
    grid[c][d] = 'B'

    display_grid(grid, "\nThis is your grid filled with your boats :")
    return grid

def turn(player, player_shots_grid, opponent_grid) :
    if player == 0 :
        display_grid(player_shots_grid,"\nThis is your previous shots :")

        print("It's your time to shoot !")
        attack = ask_position()
        e, f = attack[0], attack[1]

    else :
        print("The game master is shooting...")
        time.sleep(2)
        e = random.randint(0,2)
        f = random.randint(0,2)

    if opponent_grid[e][f] == 'B':
        print("\033[92mHit, sunk !\033[0m")
        player_shots_grid[e][f] = 'X'
        time.sleep(1)
    else :
        print("\033[91mSplash...\033[0m")
        player_shots_grid[e][f] = '.'
        time.sleep(1)
    return

def has_won(player_shots_grid) :
    count = 0
    for i in range(3):
        for j in range(3):
            if player_shots_grid[i][j] == 'X':
                count += 1
    if count == 2 :
        return True
    else :
        return False

def battleship_game() :

    print("Welcome to Battleship game!")
    print("In this game, your goal is to sink all the opponent's ships.")
    print("First you have to place your boats, then turn by turn you'll shoot the opponent's grid until you sink all his boats.")
    print("Let the game begin !")

    grid = initialise()

    print("The game Master is placing his boats...")
    grid_master = empty_grid()
    a,b,c,d = random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)
    while c == a and d == b :
        c, d = random.randint(0, 2), random.randint(0, 2)
    grid_master[a][b], grid_master[c][d] = 'B', 'B'
    time.sleep(3)

    player_shots_grid = empty_grid()
    master_shots_grid = empty_grid()

    player = 1
    while has_won(player_shots_grid) == False and has_won(master_shots_grid) == False :

        player = next_player(player)
        if player == 0 :
            turn(player, player_shots_grid, grid_master)
            has_won(player_shots_grid)

        else :
            turn(player, master_shots_grid, grid)
            has_won(master_shots_grid)

    if has_won(player_shots_grid) == True :
        print("You win!")
        print("\033[93mYou obtain a key\033[0m")
        return True

    if has_won(master_shots_grid) == True :
        print("The game master win!")
        return False


