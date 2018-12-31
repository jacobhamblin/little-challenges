from . import helpers
from lib import sort


SORTING_ALGORITHMS = ['quicksort', 'merge_sort']


def test_sorts_small_list():
    unsorted_arrays = [
        [5,4], [3,1,2], [4.2,18.9,2.1], [300,9,1], [1,4,8,3]
    ]
    for function_name in SORTING_ALGORITHMS:
        function = getattr(sort, function_name)
        for array in unsorted_arrays:
            helpers.expect_equal(function(array), sorted(array))


def test_sorts_duplicates():
    unsorted_arrays = [
        [3,1,5,5,2,8,6,5], [1,1,1], [0,-1,-3,0,-1,7]
    ]
    for function_name in SORTING_ALGORITHMS:
        function = getattr(sort, function_name)
        for array in unsorted_arrays:
            helpers.expect_equal(function(array), sorted(array))


def test_sorts_larger_lists():
    unsorted_arrays = [
        [3,1,5,2,8,6],
        [9,4,2,1,23,5,43,89,0,-12,-500],
        [-25, 0, 9.3, 2.1, 2.04, -6, 13, 18],
    ]
    for function_name in SORTING_ALGORITHMS:
        function = getattr(sort, function_name)
        for array in unsorted_arrays:
            helpers.expect_equal(function(array), sorted(array))
