def destCity(paths):
    st1 = set()
    st2 = set()

    for i in paths:
        st1.add(i[0])
        st2.add(i[0])
        st2.add(i[1])

    for i in st2:
        if i not in st1:
            return i

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
result = destCity(paths)
print(result)