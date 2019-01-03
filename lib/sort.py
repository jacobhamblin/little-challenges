from math import log

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


class Radix:
    def __init__(self, array, base=10):
        self.array = array
        self.base = base
 

    def get_digit(self, num, base, digit_num):
        return (num // base ** digit_num) % base  
 

    def make_blanks(self, size):
        return [ [] for i in range(size) ]  
 

    def split(self, array, base, digit_num):
        buckets = self.make_blanks(base)
        for num in array:
            buckets[self.get_digit(num, base, digit_num)].append(num)  
        return buckets
     

    def merge(self, array):
        new_list = []
        for sublist in array:
           new_list.extend(sublist)
        return new_list
     

    def max_abs(self, array):
        return max(abs(num) for num in array)
     

    def split_by_sign(self, array):
        buckets = [[], []]
        for num in array:
            if num < 0:
                buckets[0].append(num)
            else:
                buckets[1].append(num)
        return buckets
 

    def sort(self):
        passes = int(round(log(self.max_abs(self.array), self.base)) + 1) 
        new_list = list(self.array)
        for digit_num in range(passes):
            new_list = self.merge(self.split(new_list, self.base, digit_num))
        return self.merge(self.split_by_sign(new_list))
     
