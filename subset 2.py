#subset 2
def rec(ind,nums,ds,res):
    res.append(ds)
    for i in range(ind,len(nums)):
            if i!=ind and nums[i]==nums[i-1]: 
                continue
            rec(ds+[nums[i]],res,i+1,nums)
def subset(nums):
    res=ds=[]
    arr=nums
    rec(0,arr,ds,res)
    return res
nums=[1,1,2]
print(subset(nums))