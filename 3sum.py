#3sum
def sum(nums):
    res=[]
    n=len(nums)
    for i in range(0,n-1):
        s=set()
        for j in range(i+1,n):
            x=-(nums[i]+nums[j])
            if x in s:
                temp=[x,nums[i],nums[j]]
                temp.sort()
                if temp not in res:
                    res.append(temp)
            else:
                s.add(nums[j])
    return res
nums = [-1,0,1,2,-1,-4]
print(sum(nums))
           