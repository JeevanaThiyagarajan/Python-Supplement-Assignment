# Problem 72: Count uppercase and lowercase letters
# Find and fix the error

def count_case(text):
    upper = lower = digits = special = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
    return upper, lower, digits, special

sentence = "Hello World 123!"
u, l, d, s = count_case(sentence)
print(f"Uppercase: {u}, Lowercase: {l}, Digits: {d}, Special: {s}")
