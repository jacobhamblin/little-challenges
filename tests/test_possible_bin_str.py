from . import helpers 
from lib import possible_bin_str 


def test_empty_str():
    helpers.expect_equal(sorted(possible_bin_str.poss_recur('')), sorted(['']))
    helpers.expect_equal(sorted(possible_bin_str.poss_iter('')), sorted(['']))


def test_one_wild():
    helpers.expect_equal(
        sorted(possible_bin_str.poss_recur('10?1')),
        sorted(['1001', '1011'])
    )
    helpers.expect_equal(
        sorted(possible_bin_str.poss_iter('10?1')),
        sorted(['1001', '1011'])
    )


def test_two_wilds():
    helpers.expect_equal(
        sorted(possible_bin_str.poss_recur('10?1?')),
        sorted(['10010', '10110', '10011', '10111'])
    )
    helpers.expect_equal(
        sorted(possible_bin_str.poss_iter('10?1?')),
        sorted(['10010', '10110', '10011', '10111'])
    )
