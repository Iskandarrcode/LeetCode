accounts = [[1,5],[7,3],[3,5]]

def boy(accounts):
    ls = list()
    sum = 0
    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            sum += accounts[i][j]
        ls.append(sum)
        sum = 0
    return max(ls)

print(boy(accounts))

