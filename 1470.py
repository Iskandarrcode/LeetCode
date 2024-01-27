nums = [2,5,1,3,4,7]
n = len(nums) // 2
result = []

for i in range(n):
    result.append(nums[i])
    result.append(nums[i + n])

print(result)