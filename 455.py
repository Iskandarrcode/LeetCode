def Cooking(s, g):
    s.sort()
    g.sort()
    i, j = 0, 0
    count = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            count += 1
            i += 1
        j += 1

    return count
                    
s = [1, 1,5]
g = [1,2,4]

print(Cooking(s, g))