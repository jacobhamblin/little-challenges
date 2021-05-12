from . import helpers
from lib import word_dictionary


def test_longest_word_returns_empty_string_if_no_matching_words():
    helpers.expect_equal(word_dictionary.longest_word("asd", []), "")
    helpers.expect_equal(word_dictionary.longest_word("asd", ["ase"]), "")


def test_longest_word_no_duplicates():
    helpers.expect_equal(
        word_dictionary.longest_word("asd", ["sad", "as", "fast"]), "sad"
    )
    helpers.expect_equal(
        word_dictionary.longest_word(
            "naromd", ["donar", "moar", "dan", "random", "rockstar"]
        ),
        "random",
    )


def test_longest_word_duplicates():
    helpers.expect_equal(word_dictionary.longest_word("lilm", ["lim", "mill"]), "mill")


def test_longest_word_with_wild():
    helpers.expect_equal(
        word_dictionary.longest_word("rac*car", ["car", "race", "racecar"]), "racecar"
    )
    helpers.expect_equal(
        word_dictionary.longest_word("****", ["it", "mine", "a", "er"]), "mine"
    )
