def get_perms(permutations, remaining):
    if not len(remaining):
        return permutations
    next = remaining[0]
    new_permutations = []
    for existing_perm in permutations:
        new_perms = []
        for i in xrange(0, len(existing_perm) + 1):
            new_perm = list(existing_perm)
            new_perm.insert(i, next)
            new_perms.append(''.join(new_perm))
        new_permutations += new_perms
    return get_perms(new_permutations, remaining[1:])


def recurse(input):
    if not len(input):
        return []
    if len(input) == 1:
        return list(input)
    permutations = [input[0]]
    return list(set(get_perms(permutations, input[1:])))


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
    return list(set(permutations))
