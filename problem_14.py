# Problem 14: Check if a number is prime
# Find and fix the error

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 17

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


