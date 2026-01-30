# Problem 34: Copy a list
# Find and fix the error

original = [1, 2, 3, 4, 5]

# Make a true copy
copy = original.copy()  # or list(original)

copy.append(6)

print(f"Original: {original}")
print(f"Copy: {copy}")
