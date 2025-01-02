
def next_player(player) :
    return 1 - player

def empty_grid() :
    empty_grid = [0][0]
    for i in range(3):
        for j in range(3):
            empty_grid[i][j] = " "
    return empty_grid

def display_grid(grid,message) :
    print(message)
    for i in range(3):
        for j in range(3):
            print("| ", grid[i][j], end=" " + "| ")
        print("\n")
    print("______________")
    return

def ask_position():
    while True:
        user_input = input("Enter a position in the format row,column: ")

        parts = user_input.split(",")
        if len(parts) == 2:
            row_str, column_str = parts[0].strip(), parts[1].strip()

            row = int(row_str)
            column = int(column_str)

            if 1 <= row < 4 and 1 <= column < 4:
                return (row, column)
            else:
                print("Position out of bounds. Please enter values between 0 and 3.")
        else:
            print("Invalid format. Please enter the position as row,column (e.g.: 1,2).")




