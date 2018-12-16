def recurse(input):
    if not len(input):
        return []
    if len(input) == 1:
        return list(input)
    head = list(input[0])
    rest = input[1]
    if not type(input) == list:
        rest = input[1:]
    if not len(rest):
        return head
    next = rest[0]
    permutations = []
    for existing_perm in head:
        new_perms = []
        for i in xrange(0, len(existing_perm) + 1):
            new_perm = list(existing_perm)
            new_perm.insert(i, next)
            new_perms.append(''.join(new_perm))
        permutations += new_perms
    return recurse([permutations, rest[1:]])


def iterate(input):
    if not len(input):
        return []
    if len(input) == 1:
        return list(input)
    permutations = [input[0]]
    remaining = input[1:]
    num_remaining = len(input[1:])
    while len(remaining):
        next = remaining[0]
        remaining = remaining[1:]
        new_permutations = []
        for existing_perm in permutations:
            new_perms = []
            for i in xrange(0, len(existing_perm) + 1):
                new_perm = list(existing_perm)
                new_perm.insert(i, next)
                new_perms.append(''.join(new_perm))
            new_permutations += new_perms
        permutations = new_permutations
    return permutations
