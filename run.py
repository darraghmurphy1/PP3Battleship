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

