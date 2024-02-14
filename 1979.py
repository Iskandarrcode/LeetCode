def ekub(nums):
    ls = list()
    kat = max(nums)
    kic = min(nums)
    if kat % kic == 0:
        return kic
    
    else:
        for i in range(1, kic):
            if kat % i == 0:
                if kic % i == 0:
                    ls.append(i)
        ls.sort()
        maxx = ls[-1]
        return maxx

nums = [2,5,6,9,10]

print(ekub(nums))