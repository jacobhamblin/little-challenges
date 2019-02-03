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

def regex_match(s, pattern):
    if not pattern:
        return not s

    first_match = bool(s) and pattern[0] in {s[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (regex_match(s, pattern[2:]) or
                first_match and regex_match(s[1:], pattern))
    else:
        return first_match and regex_match(s[1:], pattern[1:])
