from lib import change
from . import helpers


def test_no_change():
    helpers.expect_equal(change.fewest_coins(0, []), [])
    helpers.expect_equal(change.fewest_coins(0, [1, 5]), [])
    helpers.expect_equal(change.fewest_coins(-5, [1, 5]), [])


def test_up_to_one_of_each_coin():
    helpers.expect_equal(change.fewest_coins(10, [1, 5, 10]), [0, 0, 1])
    helpers.expect_equal(change.fewest_coins(15, [1, 5, 10]), [0, 1, 1])
    helpers.expect_equal(change.fewest_coins(25, [1, 5, 10, 25]), [0, 0, 0, 1])


def test_multiple_of_a_coin():
    helpers.expect_equal(change.fewest_coins(29, [1, 5, 25]), [4, 0, 1])
    helpers.expect_equal(change.fewest_coins(23, [1, 5, 10]), [3, 0, 2])
    helpers.expect_equal(change.fewest_coins(18, [1, 5, 10]), [3, 1, 1])


def test_strange_coins():
    helpers.expect_equal(change.fewest_coins(13, [3, 6, 7]), [2, 0, 1])
    helpers.expect_equal(change.fewest_coins(24, [5, 8, 12]), [0, 0, 2])
