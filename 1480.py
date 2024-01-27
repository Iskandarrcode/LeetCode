nums = [1,2,3,4]
nums2 = list()
for i in range(0, len(nums)):
    summ = sum(nums[:(i + 1)])
    nums2.append(summ)
print(nums2)