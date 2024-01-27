def hammingDistance(x, y):
    xor_result = x ^ y

    distance = 0
    while xor_result:
        distance += xor_result & 1
        xor_result >>= 1

    return distance

x = 4
y = 1
result = hammingDistance(x, y)
print(result)
