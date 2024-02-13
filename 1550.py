arr = [1,2,1,1]

def toqlik(arr):
    for i in range(len(arr)):
        if i <= len(arr) - 3:
            if arr[i] % 2 != 0:
                if arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                    return True
           
    return False

print(toqlik(arr))