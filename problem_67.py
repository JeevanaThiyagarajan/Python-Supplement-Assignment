# Problem 67: Remove nth element from list
# Find and fix the error

def remove_nth_inplace(lst, n):
    if -len(lst) <= n < len(lst):
        lst.pop(n)
    return lst

numbers = [1, 2, 3, 4, 5]
remove_nth_inplace(numbers, 2)
print(numbers)  # [1, 2, 4, 5]