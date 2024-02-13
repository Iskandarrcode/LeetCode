mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]

def digonal(mat):
    sum1 = 0
    sum2 = 0
    summ = 0
    l = len(mat) // 2
    s = mat[l][l]
    for i in range(0, len(mat)):
        for j in range(i, len(mat)):
            sum1 += mat[i][j]
            break
    for i in range(0, len(mat)):
        for j in range((len(mat) - 1) - i, -1, -1):
            sum2 += mat[i][j]
            break
    if len(mat) % 2 != 0:
        summ = sum1 + sum2 - s
        return summ
    else:
        summ = sum1 + sum2
        return summ
    

print(digonal(mat))
