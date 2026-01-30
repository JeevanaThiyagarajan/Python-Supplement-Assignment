# Problem 54: Find nth Fibonacci number
# Find and fix the error

def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0  # 1st Fibonacci number
    elif n == 2:
        return 1  # 2nd Fibonacci number
    
    a, b = 0, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

print(f"10th Fibonacci number: {nth_fibonacci(10)}")