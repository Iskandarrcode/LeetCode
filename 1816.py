def truncete(s, k):
    st2 = str()
    ls = s.split(" ")
    st = str()
    for i in range(k):
        st += str(ls[i])
        st += " "
    st2 = st[:len(st)-1]
        
    return st2


s = "Hello how are you Contestant"
k = 4

print(truncete(s, k))