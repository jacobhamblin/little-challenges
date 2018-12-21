from lib import change
from . import helpers

def test_no_change():
    helpers.expect_equal(change.fewest_coins(0, []), [])
    helpers.expect_equal(change.fewest_coins(0, [1, 5]), [])
