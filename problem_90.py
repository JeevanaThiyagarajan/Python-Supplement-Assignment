# Problem 90: Find median of a list
# Find and fix the error

def find_median(lst):
    # Sort the list first
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    # If even number of elements, average the middle two
    if n % 2 == 0:
        median = (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        # If odd, take the middle element
        median = sorted_lst[n//2]
    return median

# Example list
numbers = [1, 3, 5, 7, 9]
print(f"Median: {find_median(numbers)}")  # Output: 5

# Example with even number of elements
numbers_even = [1, 3, 5, 7]
print(f"Median: {find_median(numbers_even)}")  # Output: 4.0