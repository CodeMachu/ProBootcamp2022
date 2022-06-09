import random

row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]

matrix = [row_1, row_2, row_3]

print("\nPrinting each list within the matrix")
for row in matrix:
    print(row)

matrix[1][1] = "x"

print("\nComputer draws an x at center position\nPrinting the updated matrix")
for row in matrix:
    print(row)

input_1 = int(input("\nEnter 0, 1, or 2 to select the row in the matrix\n"))

input_2 = int(input("\nEnter 0, 1, or 2 to select the position within the row\n"))

matrix[1][1] = " "

matrix[input_1][input_2] = "o"

print("\nPrinting the updated matrix")
for row in matrix:
    print(row)
