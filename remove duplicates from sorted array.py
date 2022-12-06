#remove duplicate from sorted array
def remove(nums):
    i=j=0
    n=len(nums)
    while j<n:
        if nums[i]!=nums[j]:
            nums[i+1]=nums[i]
            i+=1
        j+=1
    return i+1
l=[1,1,1,2,2,3,3]
print(remove(l))

