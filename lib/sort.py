def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[len(array) / 2]
    less = [num for num in array if num < pivot]
    more = [num for num in array if num > pivot]
    return quicksort(less) + [pivot] * array.count(pivot) + quicksort(more)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    if left_index < len(left):
        result += left[left_index:]
    if right_index < len(right):
        result += right[right_index:]
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array)/2
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

