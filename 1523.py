low = 8
high = 10

def toqlar(low, high):
    count = high - low + 1
    if low % 2 != 0 and count % 2 != 0:
        return count // 2 + 1
    else:
        return count // 2

print(toqlar(low, high))