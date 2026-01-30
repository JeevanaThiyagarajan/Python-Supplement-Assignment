# Problem 26: Add item to a list
# Find and fix the error


def add_item(list, item):
    list = list + [item]
    return list

my_list = [1, 2, 3]
my_list = add_item(my_list, 4)
print(f"List after adding: {my_list}")
