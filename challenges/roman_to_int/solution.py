def roman_to_int(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    previous_value = 0
    for c in reversed(s):
        current_value = roman_map.get(c, 0)
        if current_value < previous_value:
            total -= current_value
        else:
            total += current_value
        previous_value = current_value
    return total if total == roman_to_int_no_repeat(s) else 0

def roman_to_int_no_repeat(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_map.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
