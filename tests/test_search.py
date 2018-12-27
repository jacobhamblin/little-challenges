from . import helpers
from lib import search


def test_binary_search_small_array():
    helpers.expect_equal(search.binary([1,2,3], 2), 1)
    helpers.expect_equal(search.binary([18,20,71], 18), 0)
    helpers.expect_equal(search.binary([4,7,9], 9), 2)
