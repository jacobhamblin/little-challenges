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

def longest_substring_no_duplicate(string):
    seen = {}
    current = 0
    longest = 0
    i = 0
    while i < len(string):
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

def longest_substring_no_duplicate_linear(string):
    best = 0
    substring = ''
    for char in string:
        if char not in substring:
            substring += char
            best = max(best, len(substring))
        else:
            next_index = substring.index(char) + 1
            substring = substring[next_index:] + char
    return best

def longest_substring_two_distinct_chars_at_most(string):
    seen = set()
    current = 0
    longest = 0
    current_start = 0
    i = 0
    while i < len(string):
        letter = string[i]
        if letter not in seen and len(seen) > 1:
            if current > longest:
                longest = current
            i = current_start
            current_start = i + 1
            current = 0
            seen.clear()
        else:
            seen.add(letter)
            current += 1
        i += 1
    return longest if longest > current else current

def regex_match(s, pattern):
    if not pattern:
        return not s

    first_match = bool(s) and pattern[0] in {s[0], '.'}

    if len(pattern) > 1 and pattern[1] == '*':
        return (
            regex_match(s, pattern[2:]) or first_match
            and regex_match(s[1:], pattern)
        )
    else:
        return first_match and regex_match(s[1:], pattern[1:])

def regex_match_linear(s, pattern):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(s)
            else:
                first_match = i < len(s) and pattern[j] in {s[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    ans = first_match and dp(i + 1, j + 1)
            memo[i, j] = ans
        return memo[i, j]
    return dp(0, 0)
