def fibonacci(n):
    ls = [0, 1]
    for i in range(2, n):
        yangi = ls[-1] + ls[-2]
        ls.append(yangi)
    return ls

n = int(input("n ga qiymat kiriting: "))

res = fibonacci(n)
print(res)