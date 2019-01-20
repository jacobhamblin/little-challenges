def is_anagram(first, second):
    if not type(first) == str or not type(second) == str:
        return False
    if not len(first) == len(second):
        return False
    letters = {}
    for char in first:
        existing = letters.get(char, 0)
        letters[char] = existing + 1
    for char in second:
        existing = letters.get(char, 0)
        if existing == 0:
            return False
        letters[char] = existing - 1
    for key in letters:
        if letters[key] != 0:
            return False
    return True

def longest_substring_without_duplicate(string):
    seen = {}
    current = 0
    longest = 0
    i = 0
    while True:
        if i == len(string):
            break
        letter = string[i]
        if letter in seen:
            if current > longest:
                longest = current
            i = seen[letter]
            current = 0
            seen = {}
        else:
            seen[letter] = i
            current += 1
        i += 1
    return longest if longest > current else current
