from lib import num_interpretations
from . import helpers


def test_empty_string():
    helpers.expect_equal(num_interpretations.decode(""), 1)


def test_string_length_one():
    helpers.expect_equal(num_interpretations.decode("3"), 1)
    helpers.expect_equal(num_interpretations.decode("9"), 1)
    helpers.expect_equal(num_interpretations.decode("1"), 1)


def test_string_length_two():
    helpers.expect_equal(num_interpretations.decode("58"), 1)
    helpers.expect_equal(num_interpretations.decode("13"), 2)
    helpers.expect_equal(num_interpretations.decode("21"), 2)
    helpers.expect_equal(num_interpretations.decode("27"), 1)
    helpers.expect_equal(num_interpretations.decode("02"), 1)


def test_string_length_three():
    helpers.expect_equal(num_interpretations.decode("582"), 1)
    helpers.expect_equal(num_interpretations.decode("132"), 2)
    helpers.expect_equal(num_interpretations.decode("212"), 3)
    helpers.expect_equal(num_interpretations.decode("272"), 1)
    helpers.expect_equal(num_interpretations.decode("024"), 2)


def test_string_length_four():
    helpers.expect_equal(num_interpretations.decode("5821"), 2)
    helpers.expect_equal(num_interpretations.decode("1322"), 3)
    helpers.expect_equal(num_interpretations.decode("2121"), 4)
    helpers.expect_equal(num_interpretations.decode("2727"), 1)
    helpers.expect_equal(num_interpretations.decode("0218"), 3)
