#missing number
def missing(nums):
    n=len(nums)
    res=[0]*(n+1)
    for i in nums:
        res[i]+=1
    for i in range(n+1):
        if res[i]==0:
            return i
# nums=[3,0,1]
nums=[0,1]
print(missing(nums))