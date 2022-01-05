#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = roman_string
    if isinstance(rom, str) == 0 or rom is None:
        return 0
    dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(rom)):
        if i > 0 and dico[rom[i]] > dico[rom[i-1]]:
            result += dico[rom[i]] - 2 * dico[rom[i-1]]
        else:
            result += dico[rom[i]]
    return result
