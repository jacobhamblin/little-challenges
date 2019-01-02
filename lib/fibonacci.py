def recur(n):
    if n in [0, 1]:
        return n
    return recur(n - 2) + recur(n - 1)


def _memo(n, seen):
    if seen.get(n) is None:
        seen[n] = _memo(n - 2, seen) + _memo(n - 1, seen)
    return seen[n]


def memo(n):
    return _memo(n, {0: 0, 1: 1})


def iter(n):
    recorded = {0: 0, 1: 1}
    for num in xrange(2, n + 1):
        recorded[num] = recorded[num - 2] + recorded[num - 1]
    return recorded[n]
