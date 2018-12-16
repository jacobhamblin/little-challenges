from lib import permutations
from . import helpers 


def test_empty_string():
    helpers.expect_equal(permutations.recurse(''), [''])
