# Problem 71: Transpose a matrix
# Find and fix the error

def transpose(matrix):
    if not matrix:
        return []  # handle empty matrix
    rows = len(matrix)
    cols = len(matrix[0])
    # Ensure all rows have the same number of columns
    for row in matrix:
        if len(row) != cols:
            raise ValueError("All rows must have the same number of columns")
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]

mat = [[1, 2, 3], [4, 5, 6]]
print(f"Transposed: {transpose(mat)}")