from . import helpers
from lib import fibonacci


FUNCTIONS = fibonacci.FIBONACCI['slow'] + fibonacci.FIBONACCI['fast']


def test_small_n():
    to_test = [0, 1, 2, 5, 10]
    expected = [0, 1, 1, 5, 55]
    for index, num in enumerate(to_test):
        for function in FUNCTIONS:
            helpers.expect_equal(function(num), expected[index])
    

def test_less_small_n():
    to_test = [12, 20]
    expected = [144, 6765]
    for index, num in enumerate(to_test):
        for function in fibonacci.FIBONACCI['fast']:
            helpers.expect_equal(function(num), expected[index])
    

def test_big_n_fast_functions():
    to_test = [75, 150, 500, 1000]
    expected = [
        2111485077978050,
        9969216677189303386214405760200,
        139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125,
        43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875,
    ]
    for index, num in enumerate(to_test):
        for function in fibonacci.FIBONACCI['fast']:
            helpers.expect_equal(function(num), expected[index])
