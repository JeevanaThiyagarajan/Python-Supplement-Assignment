# Problem 99: Find maximum subarray sum
# Find and fix the error

def max_subarray_sum(arr):
    # Initialize maximum sum and current sum with first element
    max_sum = arr[0]
    current_sum = arr[0]
    
    # Loop through the rest of the array
    for i in range(1, len(arr)):
        # Either start a new subarray at arr[i] or extend the current subarray
        current_sum = max(arr[i], current_sum + arr[i])
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum: {max_subarray_sum(numbers)}")