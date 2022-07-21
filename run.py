# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


OPPONENT_GRID =  [['  '] * 5 for x in range(5)]
USER_GRID =  [['  '] * 5 for x in range(5)]

print(OPPONENT_GRID)
print(USER_GRID)


def print_grid(grid):
    print(' A  B  C  D  E')
    print('_____________')
    row_num = 1
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1

int_letters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':5}





