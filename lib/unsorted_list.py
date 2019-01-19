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
