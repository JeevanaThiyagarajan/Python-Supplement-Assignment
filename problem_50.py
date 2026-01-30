# Problem 50: Convert string to uppercase
# Find and fix the error

text = "python programming"  # fix the variable name
uppercase = ""
for char in text:
    if 'a' <= char <= 'z':   # check if lowercase
        uppercase += chr(ord(char) - 32)  # convert to uppercase
    else:
        uppercase += char
print(f"Uppercase: {uppercase}")