# Problem 96: Find two numbers that sum to target
# Find and fix the error

def two_sum(nums, target):
    seen = {}  # Dictionary to store number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Found the pair
        seen[num] = i
    return []  # No solution found

# Example usage
numbers = [2, 7, 11, 15]
print(f"Indices: {two_sum(numbers, 9)}")  # Output: [0, 1]