#!/usr/bin/python3
"""
Module provides a function that divides all elements of matrix.

Function:
    - matrix_divided(matrix, div): divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by div.

Args:
    matrix (int or float): matrix whose elements are divided.
    div (int or float): number to divide with.

Returns:
    float: new matrix of divided with.

Raises:
    TypeError: number in matrix is not float or integer.
                each row of matrix is not the same size.
                div is not a integer or float.
    ZeroDivisionError: div is equal to zero.
"""
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    if not all([len(i) == len(matrix[0]) for i in matrix]):
        raise TypeError('Each row of the matrix must have the same size')
    if not all(all([isinstance(x, (int, float)) for x in i]) for i in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    new_matrix = [[round(x / div, 2) for x in i] for i in matrix]
    return new_matrix
