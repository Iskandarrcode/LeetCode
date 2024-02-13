def minglik(n):
    st = str(n)
    ln = len(st)
    res = ""
    for i in range(ln):
        res += st[i]
        if (ln - i - 1) % 3 == 0 and i != ln - 1:
            res += "."
    return res

n = 1234567890
print(minglik(n))
