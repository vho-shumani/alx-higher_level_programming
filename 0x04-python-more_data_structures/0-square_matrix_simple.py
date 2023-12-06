#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mylist = []
    for i in matrix:
        mylist.append(list(map(lambda x: x**2, i)))
    return mylist
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

        