from collections import defaultdict
from copy import copy


def longest_word(string, list_of_words):
    longest_length = 0
    word_index = -1
    if not len(list_of_words):
        return ""
    available_letters = defaultdict(lambda: 0)
    for index in xrange(0, len(string)):
        available_letters[string[index]] += 1
    for index, word in enumerate(list_of_words):
        if len(word) > longest_length:
            word_works = True
            available_letters_copy = copy(available_letters)
            for char in word:
                available_letters_copy[char] -= 1
                if available_letters_copy[char] < 0:
                    if available_letters_copy["*"]:
                        available_letters_copy["*"] -= 1
                        available_letters_copy[char] = 0
                    else:
                        word_works = False
                        break
            if word_works:
                longest_length = len(word)
                word_index = index
    if word_index > -1:
        return list_of_words[word_index]
    return ""
