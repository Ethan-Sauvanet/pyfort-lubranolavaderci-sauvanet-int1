
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
        user_input = input("Enter a position for a boat in the format row,column: ")

        parts = user_input.split(",")
        if len(parts) == 2:
            row_str, column_str = parts[0].strip(), parts[1].strip()

            row = int(row_str) - 1
            column = int(column_str) - 1

            if 0 <= row < 3 and 0 <= column < 3:
                return (row, column)
            else:
                print("Position out of bounds. Please enter values between 1 and 3.")
        else:
            print("Invalid format. Please enter the position as row,column (e.g.: 1,2).")

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
    return

def turn(player, player_shots_grid, opponent_grid) :





