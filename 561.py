nums = [6, 2, 6, 5, 1, 2]

def min(nums):
    sum = 0
    nums.sort()
    for i in range(0, len(nums)):
        if i % 2 == 0:
            sum += nums[i]
    return sum
        
print(min(nums))