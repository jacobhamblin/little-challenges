from . import helpers
from lib import knight


expect = helpers.expect_equal
FUNCTION_NAMES = ['dialer', 'dialer_memo', 'dp']

def test_dialer():
    for function_name in FUNCTION_NAMES:
        func = getattr(knight, function_name)
        expect(func(1, 4), 3)
        expect(func(2, 4), 6)
        expect(func(3, 4), 14)
        expect(func(3, 1), 10)
        expect(func(5, 2), 48)
