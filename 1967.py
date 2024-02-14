patterns = ["a","a","a"]
word = "ab"

def inside(patterns, word):
    count = 0
    for i in range(len(patterns)):
        if patterns[i] in word:
            count += 1
    return count

print(inside(patterns, word))