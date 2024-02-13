# mat = [1, 2]
# mat = [1, 2, 3]
mat = [1,4,2,5,3]
# 58

def counts(mat):
    summ = 0
    n = len(mat)

    for i in range(1, n + 1, 2):
        for j in range(n - i + 1):
            summ += sum(mat[j:j+i])

    return summ

print(counts(mat))