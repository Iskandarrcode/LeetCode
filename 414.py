def thirdMax(nums):
    unique_nums = sorted(set(nums), reverse=True)

    if len(unique_nums) >= 3:
        return unique_nums[2]
    else:
        return unique_nums[0]

nums = [2, 4, 1, 3, 6, 4, 8, 9, 4, 7]
result = thirdMax(nums)
print(result)
