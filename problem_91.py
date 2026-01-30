# Problem 91: Implement selection sort
# Find and fix the error

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example list
numbers = [64, 25, 12, 22, 11]

# Print the sorted list
print(f"Sorted: {selection_sort(numbers)}")