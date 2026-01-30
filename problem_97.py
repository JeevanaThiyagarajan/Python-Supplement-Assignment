# Problem 97: Remove element from list
# Find and fix the error

def remove_element(nums, val):
    i = 0  # Pointer for position to write
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# Example usage
numbers = [3, 2, 2, 3, 4, 5]
length = remove_element(numbers, 3)

print(f"New length: {length}")            # Output: 4
print(f"Modified list: {numbers[:length]}")  # Output: [2, 2, 4, 5]