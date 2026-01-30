# Problem 52: Find missing number in sequence
# Find and fix the error

def find_missing(numbers):
    n = len(numbers) + 1  # total numbers including the missing one
    expected_sum = n * (n + 1) // 2  # integer division
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

nums = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(f"Missing number: {find_missing(nums)}")
