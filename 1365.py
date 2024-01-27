nums = [8,1,2,2,3]
count = 0
ls = list()

for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if nums[i] > nums[j] and nums[i] != nums[j]:
            count += 1
    ls.append(count)
    count = 0
print(ls)


# Chiqish: [4,0,1,1,3]