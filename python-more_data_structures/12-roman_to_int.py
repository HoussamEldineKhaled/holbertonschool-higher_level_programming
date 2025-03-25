#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    size = len(roman_string)
    i = 0
    while i < size:
        current_char = roman_string[i]
        current_value = roman_values[current_char]
        if i + 1 < size:
            next_char = roman_string[i + 1]
            next_value = roman_values[next_char]
            if current_value < next_value:
                result += (next_value - current_value)
                i += 2
                continue
        result += current_value
        i += 1
    return result
