num = 38566789

def add_digits(num):
    num2 = 0

    while num >= 10:
        while num > 0:
            num2 += num % 10
            num //= 10
        num = num2
        num2 = 0
    return num

print(add_digits(num))
    