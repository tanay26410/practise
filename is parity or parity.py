#remove duplicate from sorted array
def remove(nums):
    n=len(nums)
    nums.sort()
    l=[]
    for i in range(n):
        if nums[i] not in l:
            l.append(nums[i])
        else:
            l.append(nums[i])
    return l
l=['1','2','3','_','5']
print(remove(l))

