from . import helpers
from lib import strings


def test_is_anagram_edges():
    helpers.expect_equal(strings.is_anagram('', ''), True)
    helpers.expect_equal(strings.is_anagram('asd', ''), False)
    helpers.expect_equal(strings.is_anagram('asd', 3), False)
    helpers.expect_equal(strings.is_anagram(1, {}), False)
    helpers.expect_equal(strings.is_anagram(True, 'asd'), False)

def test_is_anagram_normal_cases():
    helpers.expect_equal(strings.is_anagram('asd', 'qwe'), False)
    helpers.expect_equal(strings.is_anagram('assd', 'asdd'), False)
    helpers.expect_equal(strings.is_anagram('asds', 'sads'), True)
    helpers.expect_equal(
        strings.is_anagram('i am a friend', 'a friend i am'),
        True
    )
    helpers.expect_equal(strings.is_anagram('re sd', 'dse r'), True)

def test_longest_substring_without_duplicate():
    func = strings.longest_substring_without_duplicate
    helpers.expect_equal(func('abcbabccb'), 3)
    helpers.expect_equal(func('twtadst'), 5)
    helpers.expect_equal(func('mbmookl'), 3)
    helpers.expect_equal(func(''), 0)
