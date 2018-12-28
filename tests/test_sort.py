from . import helpers
from lib import sort


SORTING_ALGORITHMS = [sort.quicksort]


def test_quicksort_sorts_small_list():
    for function in SORTING_ALGORITHMS:
        helpers.expect_equal(function([5,4]), [4,5])
        helpers.expect_equal(function([3,1,2]), [1,2,3])
        helpers.expect_equal(function([4.2,18.9,2.1]), [2.1,4.2,18.9])
        helpers.expect_equal(function([300,9,1]), [1,9,300])
        helpers.expect_equal(function([1,4,8,3]), [1,3,4,8])


def test_quicksort_sorts_duplicates():
    for function in SORTING_ALGORITHMS:
        test_arr = [3,1,5,5,2,8,6,5]
        helpers.expect_equal(function(test_arr), sorted(test_arr))


def test_quicksort_sorts_larger_lists():
    for function in SORTING_ALGORITHMS:
        test_arr = [3,1,5,2,8,6]
        helpers.expect_equal(function(test_arr), sorted(test_arr))
        test_arr = [9,4,2,1,23,5,43,89,0,-12,-500]
        helpers.expect_equal(function(test_arr), sorted(test_arr))
        test_arr = [-25, 0, 9.3, 2.1, 2.04, -6, 13, 18]
        helpers.expect_equal(function(test_arr), sorted(test_arr))
