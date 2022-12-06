#single number
def single(nums):
    res={}
    for i in nums:
            if i not in res:
                res[i]=1
            else:
                res[i]+=1
    for i in res:
        if res[i]==1:
            return i
nums=[1,2,2,1,1,2,3]
print(single(nums))