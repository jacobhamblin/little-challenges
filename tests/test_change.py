from lib import change
from . import helpers


expect = helpers.expect_equal


def test_no_change():
    helpers.expect_equal(change.fewest_coins(0, []), [])
    helpers.expect_equal(change.fewest_coins(0, [1, 5]), [0, 0])

def test_up_to_one_of_each_coin():
    helpers.expect_equal(change.fewest_coins(10, [1, 5, 10]), [0, 0, 1])
    helpers.expect_equal(change.fewest_coins(15, [1, 5, 10]), [0, 1, 1])
    helpers.expect_equal(change.fewest_coins(25, [1, 5, 10, 25]), [0, 0, 0, 1])

def test_multiple_of_a_coin():
    helpers.expect_equal(change.fewest_coins(29, [1, 5, 25]), [4, 0, 1])
    helpers.expect_equal(change.fewest_coins(23, [1, 5, 10]), [3, 0, 2])
    helpers.expect_equal(change.fewest_coins(18, [1, 5, 10]), [3, 1, 1])

def test_strange_coins():
    helpers.expect_equal(change.fewest_coins(19, [2, 7, 11]), [4, 0, 1])
    helpers.expect_equal(change.fewest_coins(13, [3, 6, 7]), [0, 1, 1])
    helpers.expect_equal(change.fewest_coins(24, [5, 8, 12]), [0, 0, 2])
    helpers.expect_equal(change.fewest_coins(28, [8, 10, 12]), [2, 0, 1])

def test_fewest_coins_num_used():
    func = change.fewest_coins_num_used
    expect(func(12, [2,3,5]), 3)
    expect(func(27, [1,4,8,12]), 5)
    expect(func(30, [2,4,5]), 6)
    expect(func(41, [1,10]), 5)

def test_no_steps():
    helpers.expect_equal(change.staircase(0, [1, 2]), 1)
    helpers.expect_equal(change.staircase(1, [2]), 0)

def test_other_one_way():
    helpers.expect_equal(change.staircase(2, [2, 3]), 1)
    helpers.expect_equal(change.staircase(1, [1, 2]), 1)

def test_standard_steps():
    helpers.expect_equal(change.staircase(4, [1, 2]), 5)
    helpers.expect_equal(change.staircase(3, [1, 2]), 3)

def test_nonstandard_steps():
    helpers.expect_equal(change.staircase(4, [3, 4]), 1)
    helpers.expect_equal(change.staircase(10, [2, 5, 7]), 2)
    helpers.expect_equal(change.staircase(3, [1, 3]), 2)
    helpers.expect_equal(change.staircase(6, [1, 3]), 6)
    helpers.expect_equal(change.staircase(30, [5, 8, 3]), 233)
