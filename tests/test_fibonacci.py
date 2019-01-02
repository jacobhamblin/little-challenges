from . import helpers
from lib import fibonacci


FAST_FUNCTIONS = ['memo', 'iter', 'iter_two']
FUNCTIONS = ['recur'] + FAST_FUNCTIONS


def test_small_n():
    to_test = [0, 1, 2, 5, 10]
    for num in to_test:
        for function_name in FUNCTIONS:
            function = getattr(fibonacci, function_name)
            function(num)
    

def test_less_small_n():
    to_test = [12, 20]
    for num in to_test:
        for function_name in FUNCTIONS:
            function = getattr(fibonacci, function_name)
            function(num)
    

def test_big_n_fast_functions():
    to_test = [75, 150, 500, 1000]
    for num in to_test:
        for function_name in FAST_FUNCTIONS:
            function = getattr(fibonacci, function_name)
            function(num)
