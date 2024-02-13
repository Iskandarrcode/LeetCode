def jam(n):
    oyn = 0
    ls = list()
    while n != 1:
        if n % 2 != 0:
            oyn = (n - 1) / 2
            ls.append(oyn)
            oyn = 0
            n = (n-1) / 2 + 1
            
        if n % 2 == 0:
            oyn = n / 2
            ls.append(oyn)
            oyn = 0
            n = n / 2
    summ = int(sum(ls))
    return summ

n = int(input("Jamolar sonini kiriting: "))
print(jam(n))