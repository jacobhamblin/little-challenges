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


def two_from_wild(str, index):
    first = list(str)
    second = list(str)
    first[index] = '0'
    second[index] = '1'
    return [''.join(first), ''.join(second)]


def binary_string_recurse(str):
    list_str = list(str)
    wilds = []
    for index, char in enumerate(list_str):
        if char == '?':
            wilds.append(index)
    strings = [str]
    if not len(wilds):
        return [str]
    else:
        poss = two_from_wild(str, wilds[0])
        return binary_string_recurse(poss[0]) + binary_string_recurse(poss[1])


def binary_string_iterate(str):
    list_str = list(str)
    wilds = []
    strings = [str]
    for index, char in enumerate(list_str):
        if char == '?':
            wilds.append(index)
    while len(wilds):
        next_index = wilds.pop(0)
        new_strings = []
        for str_index, string in enumerate(strings):
            first = list(string)
            second = list(string)
            first[next_index] = '0'
            second[next_index] = '1'
            new_strings.append(''.join(first))
            new_strings.append(''.join(second))
        strings = new_strings
    return strings
