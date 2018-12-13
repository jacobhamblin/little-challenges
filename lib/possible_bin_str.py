def poss_recur(str):
    list_str = list(str)
    wilds = []
    for index, char in enumerate(list_str):
        if char == '?':
            wilds.append(index)
    if not len(wilds):
        return [str]
    if len(wilds) == 1:
        result = []
        first = list(list_str)
        second = list(list_str)
        first[wilds[0]] = '0'
        second[wilds[0]] = '1'
        result.append(''.join(first))
        result.append(''.join(second))
        return result
    return 


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
