target = [1,2,2,3]
arr = [1,1,2,3]

def True_(target, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] in target:
            count += 1
            target.remove(arr[i])
    if count == len(arr):
        return True
    else:
        return False

print(True_(target, arr))