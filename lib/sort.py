def quicksort(list):
    if len(list) < 2:
        return list
    pivot = list[len(list) / 2]
    less = [num for num in list if num < pivot]
    more = [num for num in list if num > pivot]
    return quicksort(less) + [pivot] * list.count(pivot) + quicksort(more)
