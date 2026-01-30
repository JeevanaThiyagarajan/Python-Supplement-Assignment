# Problem 74: Find first non-repeating character
# Find and fix the error

def first_non_repeating(text):
    # Convert to lowercase to make it case-insensitive
    text_lower = text.lower()
    
    # Count letters only
    char_count = {}
    for char in text_lower:
        if char.isalpha():  # ignore digits, spaces, punctuation
            char_count[char] = char_count.get(char, 0) + 1
    
    # Find first non-repeating letter in original order
    for char in text_lower:
        if char.isalpha() and char_count[char] == 1:
            return char
    
    return None  # no non-repeating character

# Example usage
word = "Programming!"
result = first_non_repeating(word)
print(f"First non-repeating letter: {result}")