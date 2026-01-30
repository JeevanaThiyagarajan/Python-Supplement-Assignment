# Problem 46: Find product of all numbers in a list
# Find and fix the error

numbers = [2, 3, 4, 5]
product = 1  # start with 1 for multiplication
for num in numbers:
    product *= num
print(f"Product: {product}")