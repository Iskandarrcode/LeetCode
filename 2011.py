def x_lar(operations):
    X = 0
    for i in operations:
        if i == "++X" or i == "X++":
            X += 1
        elif i == "--X" or i == "X--":
            X -= 1
    return X

operations = ["++X", "--X", "X++"]
print(x_lar(operations))
