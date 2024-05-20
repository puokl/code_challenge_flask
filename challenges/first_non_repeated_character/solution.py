def first_non_repeated_character(str):
    char_count = {}
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
    for char in str:
        if char_count[char] == 1:
            return char
    return None
