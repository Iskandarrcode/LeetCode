nums = [12,345,2,6,7896]
count = 0
for i in range(0, len(nums)):
    nums[i] = str(nums[i])
    ln = len(nums[i])
    if ln % 2 == 0:
        count += 1
print(count)