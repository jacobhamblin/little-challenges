def unique_paths(m, n):
    matrix = [[0] * n for i in range(m)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            row, col = (m - i, n - j)
            if i == 1 or j == 1:
                matrix[row][col] = 1
            else:
                matrix[row][col] = matrix[row + 1][col] + matrix[row][col + 1]
    return matrix[0][0]

def out_of_boundary_paths(m, n, N, i, j):
    return 0
