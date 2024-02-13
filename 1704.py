def unli(s):
    l = len(s)
    c1 = 0
    c2 = 0
    for i in range(l // 2):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
            c1 += 1
    for j in range(l - 1, (l // 2) - 1, -1):
        if s[j] == "a" or s[j] == "e" or s[j] == "i" or s[j] == "o" or s[j] == "u" or s[j] == "A" or s[j] == "E" or s[j] == "I" or s[j] == "O" or s[j] == "U":
            c2 += 1
    
    if c1 == c2:
        return True
    else:
        return False


s = "AbCdEfGh"

print(unli(s))