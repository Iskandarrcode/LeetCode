def repeatedSubstringPattern(s):
    uzun = len(s)

    for i in range(1, uzun // 2 + 1):
        if uzun % i == 0:
            ls = s[:i]
            ls2 = uzun // i

            if ls * ls2 == s:
                return True

        return False

s = "abab"
result = repeatedSubstringPattern(s)
print(result)
