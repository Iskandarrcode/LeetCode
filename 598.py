def maxCount(m, n, ops):
    if not ops:
        return m * n
    
    min_x = min(op[0] for op in ops)
    min_y = min(op[1] for op in ops)
    
    return min_x * min_y

m = 3
n = 3
ops = [[2, 2], [3, 3]]
result = maxCount(m, n, ops)
print(result)
