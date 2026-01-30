# Problem 82: Remove adjacent duplicates
# Find and fix the error

def remove_all_duplicates(text):
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

s = "programming"
print(f"After removing all duplicates: {remove_all_duplicates(s)}")