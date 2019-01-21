from . import helpers
from lib import interviewingio


def test_things():
    expect = helpers.expect_equal
    func = interviewingio.unique_half_candies
    expect(func([3, 4, 7, 7, 6, 6]), 3)
    expect(func([80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]), 3)
