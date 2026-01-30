# Problem 25: Find GCD of two numbers
# Find and fix the error

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("GCD of 48 and 18:", gcd(48, 18))