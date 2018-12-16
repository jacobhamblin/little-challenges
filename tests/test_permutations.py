from lib import permutations
from . import helpers 


def test_empty_string():
    helpers.expect_equal(permutations.recurse(''), [])
    helpers.expect_equal(permutations.iterate(''), [])

def test_length_one():
    helpers.expect_equal(permutations.recurse('a'), ['a'])
    helpers.expect_equal(permutations.iterate('a'), ['a'])

def test_length_two():
    helpers.expect_equal(
        sorted(permutations.recurse('ab')),
        sorted(['ab', 'ba'])
    )
    helpers.expect_equal(
        sorted(permutations.iterate('ab')),
        sorted(['ab', 'ba'])
    )

def test_length_three():
    helpers.expect_equal(
        sorted(permutations.recurse('abc')),
        sorted(['abc', 'bac', 'acb', 'bca', 'cab', 'cba'])
    )
    helpers.expect_equal(
        sorted(permutations.iterate('abc')),
        sorted(['abc', 'bac', 'acb', 'bca', 'cab', 'cba'])
    )

def test_length_four():
    helpers.expect_equal(
        sorted(permutations.recurse('dceq')),
        sorted([
            'cdeq', 'cdqe', 'cedq', 'ceqd', 'cqde', 'cqed', 'dceq', 'dcqe',
            'decq', 'deqc', 'dqce', 'dqec', 'ecdq', 'ecqd', 'edcq', 'edqc',
            'eqcd', 'eqdc', 'qcde', 'qced', 'qdce', 'qdec', 'qecd', 'qedc',
        ])
    )
    helpers.expect_equal(
        sorted(permutations.iterate('dceq')),
        sorted([
            'cdeq', 'cdqe', 'cedq', 'ceqd', 'cqde', 'cqed', 'dceq', 'dcqe',
            'decq', 'deqc', 'dqce', 'dqec', 'ecdq', 'ecqd', 'edcq', 'edqc',
            'eqcd', 'eqdc', 'qcde', 'qced', 'qdce', 'qdec', 'qecd', 'qedc',
        ])
    )
