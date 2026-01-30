
numbers = [12, -5, 8, -3, 15, -9, 0]

positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive, "Negative:", negative, "Zero:", zero)