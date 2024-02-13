def findCenter(edges):
        n = edges[0][0]
        if n not in edges[1]:
            n = edges[0][1]
        return n
    
edges = [[1,2],[5,1],[1,3],[1,4]]

print(findCenter(edges))