# Problem 81: Check if string has balanced brackets
# Find and fix the error

def balanced_brackets(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:  # opening brackets
            stack.append(char)
        elif char in pairs.values():  # closing brackets
            if not stack:
                return False
            if pairs[stack[-1]] == char:  # check top of stack
                stack.pop()
            else:
                return False
    return len(stack) == 0

# Examples
expr1 = "{[()]}"
expr2 = "([)]"
expr3 = "(({}))"

print(f"{expr1} Balanced: {balanced_brackets(expr1)}")  # True
print(f"{expr2} Balanced: {balanced_brackets(expr2)}")  # False
print(f"{expr3} Balanced: {balanced_brackets(expr3)}")  # True
