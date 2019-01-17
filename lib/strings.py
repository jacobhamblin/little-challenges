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