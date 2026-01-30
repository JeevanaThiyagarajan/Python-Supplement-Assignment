# Problem 98: Check if power of two
# Find and fix the error

def is_power_of_two(n):
    if n <= 0:
        return False
    # Bitwise check: only powers of two have exactly one bit set
    return (n & (n - 1)) == 0

# Examples
print(f"Is 16 power of 2? {is_power_of_two(16)}")  # True
print(f"Is 18 power of 2? {is_power_of_two(18)}")  # False
print(f"Is 0 power of 2? {is_power_of_two(0)}")    # False
print(f"Is 1 power of 2? {is_power_of_two(1)}")    # True