from . import helpers
from lib import int_list


def test_get_mode():
    helpers.expect_equal(int_list.get_mode([1,2,3,2]), 2)
    helpers.expect_equal(
        int_list.get_mode([5,2,3,1,2,5,7,5,4]),
        5
    )
    helpers.expect_equal(
        int_list.get_mode([2,4,6,3,4,1]),
        4
    )
