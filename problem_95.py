# Problem 95: Convert Roman to Integer
# Find and fix the error

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        # If current value is less than next value, subtract it
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total

# Example
print(f"XIV = {roman_to_int('XIV')}")  # Output: 14
print(f"IX = {roman_to_int('IX')}")    # Output: 9
print(f"LVIII = {roman_to_int('LVIII')}") # Output: 58