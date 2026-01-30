# Problem 41: Find index of element in list
# Find and fix the error

nnumbers = [10, 20, 30, 40, 50]
search = 30
index = -1
for i in range(len(numbers)):
    if numbers[i] == search:
        index = i
        break  # stop loop once found
print(f"Index of {search}: {index}")