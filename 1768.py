def labrint():
    st = str()
    word1 = "ab"
    word2 = "pqrs"
    if len(word1) == len(word2):
        for i in range(len(word1)):
            st += word1[i]
            st += word2[i]
    if len(word1) > len(word2):
        for i in range(len(word1)):
            st += word1[i]
            if i < len(word2):
                st += word2[i]
    if len(word2) > len(word1):
        for i in range(len(word2)):
            if i < len(word1):
                st += word1[i]
                st += word2[i]
                
    return st
    
print(labrint())