# Problem 80: Find mode (most frequent element)
# Find and fix the error

def find_mode(lst):
    if not lst:  # handle empty list
        return None
    
    # Count frequency
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    
    max_freq = max(freq.values())
    
    # Get all items with max frequency
    modes = [key for key, value in freq.items() if value == max_freq]
    
    # If only one mode, return it; else return list of modes
    return modes[0] if len(modes) == 1 else modes

# Examples
numbers1 = [1, 2, 2, 3, 3, 3, 4]
numbers2 = [1, 1, 2, 2, 3]
numbers3 = []

print(f"Mode: {find_mode(numbers1)}")  # 3
print(f"Mode: {find_mode(numbers2)}")  # [1, 2]
print(f"Mode: {find_mode(numbers3)}")  # None