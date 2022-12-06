#top k frequent elements
def ele(nums,k):
    d={}
    for i in nums:
        d[i]=nums.count(i)
    d=dict(sorted(d.items(),key=lambda x:x[1], reverse=True))
    return list(d.keys())[:k]

    




nums=[4,1,-1,2,-1,2,3]
k=2
print(ele(nums,k))
