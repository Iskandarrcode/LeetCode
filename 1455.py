sentence = "hellohello hellohellohello"
searchWord = "ell"

s = sentence.split(" ")
for i in range(0, len(s)):
    if searchWord in s[i]:
        print(i + 1)
        break