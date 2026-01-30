# Problem 92: Check if all elements are unique
# Find and fix the error

# Function to check if all elements in a list are unique
def all_unique(lst):
    # Convert list to a set (removes duplicates) and compare lengths
    return len(lst) == len(set(lst))

# Example 1: All elements unique
numbers1 = [1, 2, 3, 4, 5]
print(f"All unique in {numbers1}? {all_unique(numbers1)}")  # True

# Example 2: List with duplicates
numbers2 = [1, 2, 3, 2, 5]
print(f"All unique in {numbers2}? {all_unique(numbers2)}")  # False