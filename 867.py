matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix[i][j])
        
print(matrix)