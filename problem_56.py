# Problem 56: Remove vowels from string
# Find and fix the error

sentence = "Hello World"
result = "".join(char for char in sentence if char.lower() not in "aeiou")
print(f"Without vowels: {result}")