def unique(nums):
    ls = list()
    for i in nums:
        if nums.count(i) == 1:
            ls.append(i)
    return sum(ls)

nums = [1,2,3,2]

print(unique(nums))