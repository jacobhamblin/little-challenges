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

# a-z -> trivial
# . == wildcard -> trivial
# (bbc, b*bc)
def regex_match(s, pattern):
    s_index = 0
    p_index = 0
    if len(s) and not len(pattern):
        return False
    while p_index < len(pattern):
        if p_index + 1 < len(pattern) and pattern[p_index + 1] == '*':
            new_str = 'a' + s[s_index:]
            increment_to_s_index = 0
            while len(new_str[1:]):
                increment_to_s_index += 1
                new_str = new_str[1:]
                match = regex_match(new_str, pattern[p_index + 2:])
                if match:
                    return True
            if not len(new_str):
                return False
            p_index += 1
            s_index += (increment_to_s_index - 1)

        elif pattern[p_index] == '.':
            if s_index >= len(s):
                return False
        else:
            if s[s_index] != pattern[p_index]:
                return False
        s_index += 1
        p_index += 1
    return True
