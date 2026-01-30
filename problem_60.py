# Problem 60: Check if number is Armstrong number
# Find and fix the error

def is_armstrong(n):
    num_str = str(n)
    return n == sum(int(d)**len(num_str) for d in num_str)

print(f"Is 153 Armstrong? {is_armstrong(153)}")