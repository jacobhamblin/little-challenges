def bin_recur(list, value):
    if not len(list):
        return -1
    mid = len(list)/2
    if list[mid] == value:
        return mid
    if list[mid] > value:
        return bin_recur(list[0:mid], value)
    else:
        rest = bin_recur(list[mid + 1:len(list)], value)
        if rest is -1:
            return -1
        return mid + 1 + rest


def _bin_recur_indices(list, value, start, end):
    if end < start:
        return -1
    mid_index = (end - start / 2) + start
    mid = list[mid_index]
    if mid == value:
        return mid_index
    if mid > value:
        return _bin_recur_indices(list, value, start, mid_index - 1)
    else:
        return _bin_recur_indices(list, value, mid_index + 1, end)


def bin_recur_indices(list, value):
    return _bin_recur_indices(list, value, 0, len(list) - 1)
