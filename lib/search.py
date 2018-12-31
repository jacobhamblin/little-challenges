def binary(list, value):
    if not len(list):
        return -1
    mid = len(list)/2
    if list[mid] == value:
        return mid
    if list[mid] > value:
        return binary(list[0:mid], value)
    else:
        rest = binary(list[mid + 1:len(list)], value)
        if rest is -1:
            return -1
        return mid + 1 + rest
