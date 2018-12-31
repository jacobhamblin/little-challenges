from . import helpers
from lib import search


def test_missing_value():
    helpers.expect_equal(search.binary([1,2,3], 5), -1)
    helpers.expect_equal(search.binary([], 1), -1)


def test_binary_search_small_array():
    helpers.expect_equal(search.binary([1,2,3], 2), 1)
    helpers.expect_equal(search.binary([18,20,71], 18), 0)
    helpers.expect_equal(search.binary([4,7,9], 9), 2)


def test_binary_search_larger_array():
    helpers.expect_equal(search.binary([1,2,3,4,5], 2), 1)
    helpers.expect_equal(search.binary([8,11,14,16,19], 16), 3)
    helpers.expect_equal(search.binary([1,3,5,7,9], 3), 1)
    helpers.expect_equal(search.binary([1,3,4,6,7,9,10], 10), 6)
