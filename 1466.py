s = "leetcode"
n = 1
for i in range(len(s)):
    if s[i] == s[i+1]:
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                n += 1