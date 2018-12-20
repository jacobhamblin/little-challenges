from lib import autocomplete
from . import helpers 


def test_simple():
    helpers.expect_equal(sorted(autocomplete.possibilities_slow(
        'as',
        ['asd', 'qwe', 'asrt']
    )), sorted(['asd', 'asrt']))
