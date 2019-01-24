from . import helpers
from lib import matrix


def test_unique_paths():
    func = matrix.unique_paths
    expect = helpers.expect_equal
    expect(func(3,2), 3)
    expect(func(7,10), 5005)
    expect(func(7,1), 1)
    expect(func(1,1), 1)
    expect(func(8,8), 3432)
