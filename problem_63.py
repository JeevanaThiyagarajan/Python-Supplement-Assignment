# Problem 63: Find longest word in a sentence
# Find and fix the error

text = "The quick brown fox jumps"
longest = max(text.split(), key=len)
print(f"Longest word: {longest}")