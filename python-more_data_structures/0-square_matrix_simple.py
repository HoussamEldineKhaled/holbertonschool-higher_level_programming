#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = []
    for i in matrix:
        new_row = []
        for num in i:
            new_row.append(num ** 2)
        sqr_matrix.append(new_row)
    return sqr_matrix
