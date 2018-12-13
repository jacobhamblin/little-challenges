def two_from_wild(str, index):
    first = list(str)
    second = list(str)
    first[index] = '0'
    second[index] = '1'
    return [''.join(first), ''.join(second)]


def poss_recur(str):
    list_str = list(str)
    wilds = []
    for index, char in enumerate(list_str):
        if char == '?':
            wilds.append(index)
    strings = [str]
    if not len(wilds):
        return [str]
    if len(wilds) == 1:
        return two_from_wild(str, wilds[0])
    else:
        poss = two_from_wild(str, wilds[0])
        return poss_recur(poss[0]) + poss_recur(poss[1])


def poss_iter(str):
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
