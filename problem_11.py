# Problem 11: Count occurrences of each character
# Find and fix the error

numbers = [45, 12, 78, 34, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
