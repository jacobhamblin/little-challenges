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


def out_of_bounds(m, n, i, j):
    if i < 0 or i >= m or j < 0 or j >= n:
        return True
    return False


def out_of_boundary_paths(m, n, N, i, j):
    moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
    if N == 0:
        return 0
    count = 0
    for index, move in enumerate(moves):
        new_pos = (i + move[0], j + move[1])
        if out_of_bounds(m, n, new_pos[0], new_pos[1]):
            count += 1
        else:
            count += out_of_boundary_paths(m, n, N - 1, i + move[0], j + move[1])
    return count


def out_of_boundary_paths_memo(m, n, N, i, j):
    memo = {}
    moves = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def helper(N, i, j):
        if (N, i, j) in memo:
            return memo[(N, i, j)]
        if N == 0:
            return 0
        count = 0
        for index, move in enumerate(moves):
            new_pos = (i + move[0], j + move[1])
            if out_of_bounds(m, n, new_pos[0], new_pos[1]):
                count += 1
            else:
                count += helper(N - 1, i + move[0], j + move[1])
        memo[(N, i, j)] = count
        return count

    return helper(N, i, j)


def out_of_bounds_dp(m, n, N, i, j):
    moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
    row = [0] * n
    matrix = []
    for index in xrange(m):
        matrix.append(row)
    while N > 0:
        for row in xrange(0, m):
            if N is 1:
                if row is 0 or row is m - 1:
                    count = 1
            for col in xrange(0, n):
                if N is 1:
                    if col is 0 or col is n - 1:
                        count += 1
                else:
                    count = matrix[row][col]
                    for move in moves:
                        new_pos = (row + move[0], col + move[1])
                        if not out_of_bounds(m, n, new_pos[0], new_pos[1]):
                            count += matrix[new_pos[0]][new_pos[1]]
                print(count)
                matrix[row][col] = count
        N -= 1
    print(matrix)
    return matrix[i][j]
