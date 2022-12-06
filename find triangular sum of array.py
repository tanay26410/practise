#find triangular sum of array
def trsum(nums):
    new=[]
    k=len(nums)
    while k>1:
        for i in range(len(nums)-1):
            new.append((nums[i]+nums[i+1])%10)
        nums=[]
        nums.extend(new)
        new=[]
        
        k-=1
    return nums
    
nums=[1,2,3,4,5]
print(trsum(nums))