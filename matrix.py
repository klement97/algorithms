from copy import deepcopy


def transpose(matrix: list) -> list:
    transposed = deepcopy(matrix)
    row_len = len(matrix)
    column_len = len(matrix[0])

    for i in range(row_len):
        for j in range(column_len):
            transposed[i][j] = matrix[j][i]

    return transposed


def unit_matrix(n: int) -> list:
    matrix = [n * [0] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1

    return matrix
