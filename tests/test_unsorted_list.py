from . import helpers
from lib import unsorted_list

KTH_SMALLEST_FUNCTIONS = ['kth_smallest', 'kth_smallest_in_place']

def test_kth_smallest_edges():
    for function_name in KTH_SMALLEST_FUNCTIONS:
        func = getattr(unsorted_list, function_name)
        helpers.expect_equal(func([3], 2), None)
        helpers.expect_equal(func([3, 3, 4], 1), 3)
        helpers.expect_equal(func([], 1), None)
        helpers.expect_equal(func([3, 3, 4, 5, 3, 5, 3], 1), 3)

def test_kth_smallest_basics():
    for function_name in KTH_SMALLEST_FUNCTIONS:
        func = getattr(unsorted_list, function_name)
        helpers.expect_equal(func([3], 1), 3)
        helpers.expect_equal(func([3,1,2], 1), 1)
        helpers.expect_equal(func([3,1,2,-1], 1), -1)
        helpers.expect_equal(func([3,1,2,-1], 2), 1)
        helpers.expect_equal(func([3,1,2,-1], 3), 2)
        helpers.expect_equal(func([3,1,2,-1], 4), 3)
        helpers.expect_equal(func([3,1,2,-1,4], 1), -1)
        helpers.expect_equal(func([3,1,2,-1,4], 2), 1)
        helpers.expect_equal(func([3,1,2,-1,4], 3), 2)
        helpers.expect_equal(func([3,1,2,-1,4], 4), 3)
        helpers.expect_equal(func([3,1,2,-1,4], 5), 4)
    
def test_kth_largest_edges():
    func = unsorted_list.kth_largest
    helpers.expect_equal(func([3], 2), None)
    helpers.expect_equal(func([3, 3, 2], 1), 3)
    helpers.expect_equal(func([], 1), None)
    helpers.expect_equal(func([3, 3, 4, 5, 3, 5, 3], 1), 5)

def test_kth_largest_basics():
    func = unsorted_list.kth_largest
    helpers.expect_equal(func([3], 1), 3)
    helpers.expect_equal(func([3,1,2], 1), 3)
    helpers.expect_equal(func([3,1,2,-1,4], 1), 4)
    helpers.expect_equal(func([3,1,2,-1,4], 3), 2)
    
def test_largest_sum_non_adjacent():
    func = unsorted_list.largest_sum_non_adjacent
    helpers.expect_equal(func([2, 4, 6, 2, 5]), 13)
    helpers.expect_equal(func([5, 1, 1, 5]), 10)
    helpers.expect_equal(func([1, 2, 5, 8, 1]), 10)
    helpers.expect_equal(func([-1, -10, 5, 2, -3, 4]), 9)
