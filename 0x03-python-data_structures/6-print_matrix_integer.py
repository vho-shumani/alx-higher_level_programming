#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print(1)
    else:
        for i in matrix:
            for j in range(len(i)):
                print("{:d}".format(i[j]), end=" " if j < len(i) - 1 else "\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print_matrix_integer()