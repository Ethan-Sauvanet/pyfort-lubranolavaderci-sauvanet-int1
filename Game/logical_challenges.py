
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

def ask_position() :
