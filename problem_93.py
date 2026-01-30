# Problem 93: Find longest common prefix
# Find and fix the error

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as prefix
    prefix = strs[0]
    
    # Compare with the rest of the strings
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # Shorten the prefix
            if not prefix:
                return ""  # No common prefix
    return prefix

# Example list of words
words = ["flower", "flow", "flight"]
print(f"Longest common prefix: {longest_common_prefix(words)}")  # Output: "fl"