# Problem 6: Reverse a string
# Find and fix the error


text = "Python"
reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print("Reversed:", reversed_text)
