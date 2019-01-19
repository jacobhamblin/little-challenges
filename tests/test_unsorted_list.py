from . import helpers
from lib import unsorted_list


def test_kth_smallest_edges():
    func = unsorted_list.kth_smallest
    helpers.expect_equal(func([3], 2), None)
    helpers.expect_equal(func([3, 3, 4], 1), 3)
    helpers.expect_equal(func([], 1), None)
    helpers.expect_equal(func([3, 3, 4, 5, 3, 5, 3], 1), 3)

def test_kth_smallest_basics():
    func = unsorted_list.kth_smallest
    helpers.expect_equal(func([3], 1), 3)
    helpers.expect_equal(func([3,1,2], 1), 1)
    helpers.expect_equal(func([3,1,2,-1,4], 1), -1)
    helpers.expect_equal(func([3,1,2,-1,4], 3), 2)
    
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
    
