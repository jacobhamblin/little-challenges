from lib import num_interpretations


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_empty_string():
    expect_equal(num_interpretations.decode(''), 1)


def test_string_length_one():
    expect_equal(num_interpretations.decode('3'), 1)
    expect_equal(num_interpretations.decode('9'), 1)
    expect_equal(num_interpretations.decode('1'), 1)
