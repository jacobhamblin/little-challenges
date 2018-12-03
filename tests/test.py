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


def test_string_length_two():
    expect_equal(num_interpretations.decode('58'), 1)
    expect_equal(num_interpretations.decode('13'), 2)
    expect_equal(num_interpretations.decode('21'), 2)
    expect_equal(num_interpretations.decode('27'), 1)
    expect_equal(num_interpretations.decode('02'), 1)


def test_string_length_three():
    expect_equal(num_interpretations.decode('582'), 1)
    expect_equal(num_interpretations.decode('132'), 2)
    expect_equal(num_interpretations.decode('212'), 3)
    expect_equal(num_interpretations.decode('272'), 1)
    expect_equal(num_interpretations.decode('024'), 2)


def test_string_length_four():
    expect_equal(num_interpretations.decode('5821'), 2)
    expect_equal(num_interpretations.decode('1322'), 3)
    expect_equal(num_interpretations.decode('2121'), 4)
    expect_equal(num_interpretations.decode('2727'), 1)
    expect_equal(num_interpretations.decode('0218'), 3)
