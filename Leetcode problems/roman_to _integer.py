def romanToInteger(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for char in s:
        value = roman_numerals[char]
        if value > prev_value:
            total += value - 2 * prev_value 
        else:
            total += value
        prev_value = value
    return total

if __name__ == "__main__":  
    roman_string = "MCMXCIV" 
    result = romanToInteger(roman_string)
    print(f"The integer value of the Roman numeral '{roman_string}' is: {result}")