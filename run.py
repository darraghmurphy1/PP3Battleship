# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint
OPPONENT_GRID = [[' '] * 5 for i in range(5)]
USER_GRID = [[' '] * 5 for i in range(5)]


int_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


def startup_message():
    print("Welcome to Battleships")


startup_message()


def print_grid(grid):
    print('  A B C D E')
    print(' ___________')
    row_num = 1
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def create_ships(grid):
    for ship in range(5):
        ship_row, ship_column = randint(0, 4), randint(0, 4)
        while grid[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        grid[ship_row][ship_column] = "X"


def get_ship_location():
    row = input("Enter the row you want to bomb: ").upper()
    while row not in "12345":
        print('Please enter a valid co-ordinate')
        row = input("Enter a row 1-5: ").upper()
    column = input("Enter the column you want to bomb: ").upper()
    while column not in "ABCDE":
        print('Please enter a a valid co-ordinate')
        column = input("Enter a value A-E: ").upper()
    return int(row) - 1, int_letters[column]


def count_hit_ships(grid):
    count = 0
    for row in grid:
        for column in row:
            if column == "X":
                count += 1
    return count


if __name__ == "__main__":
    create_ships(OPPONENT_GRID)
    turns = 15
    while turns > 0:
        print('Enter the co-ordinates you want to bomb')
        print_grid(USER_GRID)
        row, column = get_ship_location()
        if USER_GRID[row][column] == "O":
            print("Location already hit")
        elif OPPONENT_GRID[row][column] == "X":
            print("HIT")
            USER_GRID[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS! RELOAD!")
            USER_GRID[row][column] = "O"   
            turns -= 1     
        if count_hit_ships(USER_GRID) == 5:
            print("Congratultions! You sunk my battleship.")
            break
        print("You have " + str(turns) + " bombs left")
        if turns == 0:
            print("Game Over! You have been defeated.")