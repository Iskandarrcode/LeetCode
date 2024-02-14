word = "abcdefd"
ch = "d"

def teskari(word, ch):
    ind = 0
    st = str()
    st2 = str()
    for i in range(0, len(word)):
        if word[i] == ch:
            ind = i + 1
            break
    st = word[:ind]
    st2 = st[::-1] + word[ind:]
    return st2
    
    
print(teskari(word, ch))
            
            