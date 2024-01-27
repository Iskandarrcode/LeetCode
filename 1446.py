s = "leetcode"

def takror(s):
    count = 1
    ls = list()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[i + 1]:
                if s[i] == s[j]:
                    count += 1
        if count > 1:
            ls.append(count)
            count = 1
                
    return max(ls)
print(takror(s))
        