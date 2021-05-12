MOVE_MAP = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
    0: [1, 3],
}


def dialer(n, pos):
    if n is 0:
        return 1
    move_sums = [dialer(n - 1, move) for move in MOVE_MAP[pos]]
    return sum(move_sums)


def dialer_memo(n, pos):
    memo = {
        (0, 1): 1,
        (0, 2): 1,
        (0, 3): 1,
        (0, 4): 1,
        (0, 5): 1,
        (0, 6): 1,
        (0, 7): 1,
        (0, 8): 1,
        (0, 9): 1,
        (0, 0): 1,
    }

    def helper(n, pos):
        if (n, pos) in memo:
            return memo[(n, pos)]
        move_sums = [helper(n - 1, move) for move in MOVE_MAP[pos]]
        memo[(n, pos)] = sum(move_sums)
        return memo[(n, pos)]

    return helper(n, pos)


def dp(n, pos):
    prior_case = [1] * 10
    current_case = [0] * 10
    cur_hops = 0
    while cur_hops < n:
        current_case = [0] * 10
        cur_hops += 1

        for col in range(0, 10):
            for move in MOVE_MAP[col]:
                current_case[col] += prior_case[move]
        prior_case = current_case
    return current_case[pos]
