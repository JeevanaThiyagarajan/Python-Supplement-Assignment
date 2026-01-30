# Problem 87: Generate Pascal's triangle
# Find and fix the error

def pascals_triangle(n):
    triangle = []
    for i in range(n):
        # Start each row with 1s
        row = [1] * (i + 1)
        # Compute the inner elements
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

# Number of rows
n = 5
triangle = pascals_triangle(n)

# Print the triangle nicely
print(f"Pascal's triangle ({n} rows):")
for row in triangle:
    print(row)