# Problem 86: Find sum of matrix diagonals
# Find and fix the error

def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]             # Main diagonal
        total += matrix[i][n - 1 - i]     # Secondary diagonal

    # If n is odd, subtract the middle element once (it was counted twice)
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]

    return total

# Example matrix
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Diagonal sum: {diagonal_sum(mat)}")