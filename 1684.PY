def counts():
    a = 0
    count = 0
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    for i in range(len(words)):
        for j in range(len(words[i])):
           if words[i][j] in allowed:
               a += 1
               if a == len(words[i]):
                   count += 1
        a = 0
    return count
        
    
print(counts())