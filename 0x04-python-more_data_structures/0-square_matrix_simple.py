#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_value(x):
        return x ** 2
    new_matrix = list(map(lambda row: list(map(square_value, row)),  matrix))

    return new_matrix
