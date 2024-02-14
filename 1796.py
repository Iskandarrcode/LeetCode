s = "xyz"

def two_max(s):
    a = 0
    ls = list()
    for i in s:
        if i.isdigit():
            a += 1
            ls.append(int(i))
    
    if a == 0:
        return -1
    
    ls = set(ls)
    if len(ls) == 1:
        return -1
    ls = list(ls)
    ls.sort()
    n = ls[-2]
    return n

print(two_max(s))