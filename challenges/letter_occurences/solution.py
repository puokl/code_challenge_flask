def letter_occurrences(str):
    occurrences = {}
    for char in str:
        if char.isalpha():
            char_lower = char.lower()
            occurrences[char_lower] = occurrences.get(char_lower, 0) + 1
    return occurrences
