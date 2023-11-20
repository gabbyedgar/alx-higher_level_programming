#!/usr/bin/python3
"""Contains function to convert Roman numerals into its integer value."""


def roman_to_int(roman_string):
    """Converts Roman numeral string to an integer.

    Args:
        roman_string (str): String of Roman numerals to convert

    Returns: integer value of string, or 0 if not possible to convert.
    """
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman_string = roman_string.upper()
    val = 0
    i = 0
    while i < len(roman_string):
        n0 = numerals[roman_string[i]]
        try:
            n1 = numerals[roman_string[i + 1]]
        except IndexError:
            val += n0
            return val
        if n0 < n1:
            val += n1 - n0
            i += 1
        else:
            val += n0
        i += 1
    return val
