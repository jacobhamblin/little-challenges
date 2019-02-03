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
    func = strings.longest_substring_without_duplicate
    expect(func('abcbabccb'), 3)
    expect(func('twtadst'), 5)
    expect(func('mbmbookl'), 3)
    expect(func(''), 0)

def test_regex_match():
    func = strings.regex_match
    expect(func('ab', 'ab'), True)
    expect(func('abc', 'a.c'), True)
    expect(func('bbc', 'b*bc'), True)
    expect(func('bbc', 'b.*'), True)
    expect(func('', '.*'), True)
    expect(func('', '.'), False)
    expect(func('ab', 'ba'), False)

