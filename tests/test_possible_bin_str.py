from lib import possible_bin_str 


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_empty_str():
    expect_equal(sorted(possible_bin_str.poss_recur('')), sorted(['']))
    expect_equal(sorted(possible_bin_str.poss_iter('')), sorted(['']))


def test_one_wild():
    expect_equal(
        sorted(possible_bin_str.poss_recur('10?1')),
        sorted(['1001', '1011'])
    )
    expect_equal(
        sorted(possible_bin_str.poss_iter('10?1')),
        sorted(['1001', '1011'])
    )


def test_two_wilds():
    expect_equal(
        sorted(possible_bin_str.poss_recur('10?1?')),
        sorted(['10010', '10110', '10011', '10111'])
    )
    expect_equal(
        sorted(possible_bin_str.poss_iter('10?1?')),
        sorted(['10010', '10110', '10011', '10111'])
    )
