from . import helpers
from lib import strings


expect = helpers.expect_equal


def test_is_anagram_edges():
    expect(strings.is_anagram('', ''), True)
    expect(strings.is_anagram('asd', ''), False)
    expect(strings.is_anagram('asd', 3), False)
    expect(strings.is_anagram(1, {}), False)
    expect(strings.is_anagram(True, 'asd'), False)

def test_is_anagram_normal_cases():
    expect(strings.is_anagram('asd', 'qwe'), False)
    expect(strings.is_anagram('assd', 'asdd'), False)
    expect(strings.is_anagram('asds', 'sads'), True)
    expect(
        strings.is_anagram('i am a friend', 'a friend i am'),
        True
    )
    expect(strings.is_anagram('re sd', 'dse r'), True)

def test_longest_substring_without_duplicate():
    FUNCTION_NAMES = {
        'longest_substring_no_duplicate', 'longest_substring_no_duplicate_linear'
    }
    for function_name in FUNCTION_NAMES:
        func = getattr(strings, function_name)
        expect(func('abcbabccb'), 3)
        expect(func('twtadst'), 5)
        expect(func('mbmbookl'), 3)
        expect(func(''), 0)

def test_regex_match():
    FUNCTION_NAMES = {'regex_match', 'regex_match_linear'}
    for function_name in FUNCTION_NAMES:
        func = getattr(strings, function_name)
        expect(func('ab', 'ab'), True)
        expect(func('abc', 'a.c'), True)
        expect(func('bbc', 'b*bc'), True)
        expect(func('bbc', 'b.*'), True)
        expect(func('', '.*'), True)
        expect(func('', '.'), False)
        expect(func('abab', 'a*b*c'), False)
        expect(func('abab', 'a*b*'), False)
        expect(func('ab', 'ba'), False)

