def fibonacci(n):
    ls = [0, 1]
    for i in range(2, n + 2):
        yangi = ls[-1] + ls[-2]
        ls.append(yangi)
    return ls[-1]

n = int(input("n ga qiymat kiriting: "))

res = fibonacci(n)
print(res)