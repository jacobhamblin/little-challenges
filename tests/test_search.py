from . import helpers
from lib import search


FUNCTIONS = ['bin_recur', 'bin_recur_indices']


def test_missing_value():
    for function_name in FUNCTIONS:
        function = getattr(search, function_name)
        helpers.expect_equal(function([1,2,3], 5), -1)
        helpers.expect_equal(function([], 1), -1)


def test_binary_search_small_array():
    for function_name in FUNCTIONS:
        function = getattr(search, function_name)
        helpers.expect_equal(function([1,2,3], 2), 1)
        helpers.expect_equal(function([18,20,71], 18), 0)
        helpers.expect_equal(function([4,7,9], 9), 2)


def test_binary_search_larger_array():
    for function_name in FUNCTIONS:
        function = getattr(search, function_name)
        helpers.expect_equal(function([1,2,3,4,5], 2), 1)
        helpers.expect_equal(function([8,11,14,16,19], 16), 3)
        helpers.expect_equal(function([1,3,5,7,9], 3), 1)
        helpers.expect_equal(function([1,3,4,6,7,9,10], 10), 6)
