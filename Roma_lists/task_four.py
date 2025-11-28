# def check(row, column):
#
#     for i in range(10):
#         new_lst = []
#         return new_lst
#
# print(check(10, 10))

"""

"""
from typing import List


# row_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# row_two = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# row_three = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# my_list.append(row_one)
# my_list.append(row_two)
# my_list.append(row_three)

def create_matrix() -> List[List[int]]:
    matrix = []
    for row in range(1, 11):
        matrix_row = []
        for column in range(1, 11):
            matrix_row.append((row - 1) * 10 + column)
        matrix.append(matrix_row)

    return matrix

def crop_matrix(matrix: List[List[int]] ,row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    new_list = []

    for row in range(row_start, row_end + 1):
        new_list_row = []
        for column in range(column_start, column_end + 1):
            new_list_row.append(matrix[row][column])

        new_list.append(new_list_row)

    return new_list


def print_list(matrix: List[List[int]]):
    max_width = max(len(str(num)) for row in matrix for num in row)
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(str(matrix[row][column]).rjust(max_width), end=' ')
        print()

def spiral_print(matrix: List[List[int]]):
    row_print_left_to_right(matrix, 0, 2, 3)

def row_print_left_to_right(matrix: List[List[int]], row: int ,row_start: int, row_end: int):
    for column_index in range(row_start, row_end):
        print(matrix[row][column_index], end=' ')

initial_matrix = create_matrix()
croped_matrix = crop_matrix(initial_matrix, 2,4,3, 7)
spiral_print(initial_matrix)
print()
print_list(initial_matrix)
