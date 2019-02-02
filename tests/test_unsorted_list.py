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

def test_pairs_add_to_k():
    FUNCTION_NAMES = ['pairs_add_to_k', 'pairs_add_to_k_linear']
    for function_name in FUNCTION_NAMES:
        func = getattr(unsorted_list, function_name)
        helpers.expect_equal(func([2,5,3,1,7], 8), set(((5,3), (1,7))))
        helpers.expect_equal(func([3,4,2,5,8,6], 10), set(((4,6), (2,8))))
        helpers.expect_equal(func([8,3,4,8,2,6,8], 10), set(((4,6), (8,2))))

def test_merge_sorted_lists():
    expectations = [
        [
            [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
            [10, 12, 15, 15, 17, 20, 20, 30, 32]
        ],
        [ [[1]], [1], ],
        [ [[]], [], ],
    ]
    expect = helpers.expect_equal
    FUNCTION_NAMES = {'merge_sorted_lists_kn_log_kn', 'merge_sorted_lists_kn_log_k'}
    for function_name in FUNCTION_NAMES:
        func = getattr(unsorted_list, function_name)
        for expectation in expectations:
            expect(func(expectation[0]), expectation[1])
