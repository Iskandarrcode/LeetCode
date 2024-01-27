def arrayPairSum(nums):
    nums.sort()
    
    res = sum(nums[i] for i in range(0, len(nums), 2))
    
    return res

nums = [1, 4, 3, 2]
max = arrayPairSum(nums)
print(max)
