from . import helpers
from lib import sort


def test_quicksort_sorts_small_list():
    helpers.expect_equal(sort.quicksort([5,4]), [4,5])
    helpers.expect_equal(sort.quicksort([3,1,2]), [1,2,3])
    helpers.expect_equal(sort.quicksort([4.2,18.9,2.1]), [2.1,4.2,18.9])
    helpers.expect_equal(sort.quicksort([300,9,1]), [1,9,300])
    helpers.expect_equal(sort.quicksort([1,4,8,3]), [1,3,4,8])


def test_quicksort_sorts_duplicates():
    test_arr = [3,1,5,5,2,8,6,5]
    helpers.expect_equal(sort.quicksort(test_arr), sorted(test_arr))


def test_quicksort_sorts_larger_lists():
    test_arr = [3,1,5,2,8,6]
    helpers.expect_equal(sort.quicksort(test_arr), sorted(test_arr))
    test_arr = [9,4,2,1,23,5,43,89,0,-12,-500]
    helpers.expect_equal(sort.quicksort(test_arr), sorted(test_arr))
    test_arr = [-25, 0, 9.3, 2.1, 2.04, -6, 13, 18]
    helpers.expect_equal(sort.quicksort(test_arr), sorted(test_arr))
