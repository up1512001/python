#
#
#


number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
# accessing 2D grid first is row and second is column
#print(number_grid[0][2])
# using nested for loops or while loops we can print this while number_grid
for row in number_grid:
    for column in row:
        print(column)
# by print(number_grid) you will get whole 2D array printed as lists
# and by for loop you will get each element printed without list

