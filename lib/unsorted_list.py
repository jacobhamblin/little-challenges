def kth_smallest(unsorted_list, k):
    if k > len(unsorted_list):
        return None
    if len(unsorted_list) == 1:
        return unsorted_list[0]
    first_item = unsorted_list[0]
    greater = [num for num in unsorted_list if num > first_item]
    lesser = [num for num in unsorted_list if num < first_item]
    first_item_count = unsorted_list.count(first_item)
    new_arr = lesser + [first_item] * first_item_count + greater
    if k <= len(lesser):
        return kth_smallest(lesser, k)
    elif k > len(lesser) + first_item_count:
        return kth_smallest(greater, k - (len(lesser) + first_item_count))
    else:
        return first_item


def kth_smallest_in_place(arr, k):
    if k > len(arr):
        return None
    if len(arr) == 1:
        return arr[0]
    pivot_index = 0
    for ind in range(1, len(arr)):
        if arr[ind] < arr[pivot_index]:
            val = arr.pop(ind)
            arr.insert(0, val)
            pivot_index += 1
    pivot_count = arr.count(arr[pivot_index])
    if k < pivot_index + 1:
        return kth_smallest_in_place(arr[:pivot_index], k)
    elif k > pivot_index + pivot_count:
        return kth_smallest_in_place(
            arr[pivot_index + pivot_count :], k - (pivot_index + pivot_count)
        )
    else:
        return arr[pivot_index]


def kth_largest(unsorted_list, k):
    if k > len(unsorted_list):
        return None
    if len(unsorted_list) == 1:
        return unsorted_list[0]
    first_item = unsorted_list[0]
    greater = [num for num in unsorted_list if num > first_item]
    lesser = [num for num in unsorted_list if num < first_item]
    first_item_count = unsorted_list.count(first_item)
    new_arr = lesser + [first_item] * first_item_count + greater
    if k <= len(greater):
        return kth_largest(greater, k)
    elif k > len(greater) + first_item_count:
        return kth_largest(lesser, k - (len(greater) + first_item_count))
    else:
        return first_item


def largest_sum_non_adjacent(arr):
    inc = 0
    exc = 0

    for n in arr:
        new_exc = inc if inc > exc else exc
        inc = exc + n
        exc = new_exc

    return exc if exc > inc else inc


def pairs_add_to_k(arr, k):
    pairs = set()
    for first in range(0, len(arr)):
        for second in range(first + 1, len(arr)):
            if arr[first] + arr[second] == k:
                if (arr[second], arr[first]) not in pairs:
                    pairs.add((arr[first], arr[second]))
    return pairs


def pairs_add_to_k_linear(arr, k):
    pairs = set()
    partials = set()
    for num in arr:
        if k - num in partials:
            pairs.add((k - num, num))
            partials.remove(k - num)
        else:
            partials.add(num)
    return pairs


def merge_sorted_lists_kn_log_kn(arrs):
    flat = [el for arr in arrs for el in arr]
    return sorted(flat)


def merge_sorted_lists_kn_log_k(arrs):
    num_arrs = len(arrs)
    positions = [0] * num_arrs
    merged = []
    if not num_arrs or not len(arrs[0]):
        return merged
    unfinished = [True] * num_arrs
    while any(unfinished):
        arr_index_with_min = 0
        min_num = 999999
        for arr_index in range(len(arrs)):
            if unfinished[arr_index] == False:
                continue
            index_to_consider = positions[arr_index]
            if arrs[arr_index][index_to_consider] < min_num:
                arr_index_with_min = arr_index
                min_num = arrs[arr_index][index_to_consider]
        merged.append(min_num)
        positions[arr_index_with_min] += 1
        if positions[arr_index_with_min] >= len(arrs[0]):
            unfinished[arr_index_with_min] = False
    return merged
