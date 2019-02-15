from . import helpers
from lib import knight


expect = helpers.expect_equal


def test_dialer():
    expect(knight.dialer(3, 1), 5)
    expect(knight.dialer(3, 4), 4)

