def String(s, indices):
    res = [''] * len(s)

    for i in range(len(s)):
        res[indices[i]] = s[i]

    return ''.join(res)

s = "abcde"
indices = [4, 3, 2, 1, 0]

print(String(s, indices))
