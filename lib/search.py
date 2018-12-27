def binary(list, value):
    mid = len(list)/2
    if list[mid] == value:
        return mid
    if list[mid] > value:
        return binary(list[0:mid], value)
    else:
        return mid + 1 + binary(list[mid + 1:len(list)], value)
