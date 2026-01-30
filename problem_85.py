# Problem 85: Implement bubble sort
# Find and fix the error

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example list
numbers = [64, 34, 25, 12, 22, 11, 90]

# Print the sorted list
print(f"Sorted: {bubble_sort(numbers)}")
