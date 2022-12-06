#majority element 2
def majority2(nums):
    n = len(nums)
    c = n//3
    h = {}
    ans = []
    for i in nums:
        if i in h:
            h[i]+=1
        else:
                h[i]=1
    for j in h:
            if h[j]>c:
                ans.append(j)
    return ans
nums=[-1,-1,-1]
print(majority2(nums))