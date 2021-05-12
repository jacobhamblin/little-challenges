from . import helpers
from lib import matrix


expect = helpers.expect_equal


def test_unique_paths():
    func = matrix.unique_paths
    expect(func(3, 2), 3)
    expect(func(7, 10), 5005)
    expect(func(7, 1), 1)
    expect(func(1, 1), 1)
    expect(func(8, 8), 3432)


def test_out_of_boundary_paths():
    FUNCTION_NAMES = [
        "out_of_boundary_paths",
        "out_of_boundary_paths_memo",
        #  'out_of_bounds_dp',
    ]
    for function_name in FUNCTION_NAMES:
        func = getattr(matrix, function_name)
        expect(func(2, 2, 1, 0, 0), 2)
        expect(func(2, 2, 2, 0, 0), 6)
        expect(func(1, 3, 3, 0, 1), 12)
