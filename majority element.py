#majority element 
def majority(nums):
    res=[0]*(max(nums)+1)
    for i in nums:
            res[i]+=1
    ma=max(res)
    a=res.index(ma)
    return a
nums=[3,2,3]
print(majority(nums))