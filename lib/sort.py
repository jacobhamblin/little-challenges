def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[len(array) / 2]
    less = [num for num in array if num < pivot]
    more = [num for num in array if num > pivot]
    return quicksort(less) + [pivot] * array.count(pivot) + quicksort(more)


def _quicksort_in_place(array, start, end):
    if end - start > 0:
        pivot = array[start]
        left = start
        right = end
        while array[start] < pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
        _quicksort_in_place(array, start, right)
        _quicksort_in_place(array, left, end)


def quicksort_in_place(array):
    _quicksort_in_place(array, 0, len(array) - 1)
    return array


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


def insertion(array):
    for i in xrange(1, len(array)):
        j = i - 1
        key = array[i]
        while (array[j] > key) and (j >= 0):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
