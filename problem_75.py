# Problem 75: Check if parentheses are balanced
# Find and fix the error

def are_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Examples
expr1 = "((a + b) * (c - d))"
expr2 = "{[()()]}"
expr3 = "([)]"

print(f"{expr1} Balanced: {are_balanced(expr1)}")  # True
print(f"{expr2} Balanced: {are_balanced(expr2)}")  # True
print(f"{expr3} Balanced: {are_balanced(expr3)}")  # False
