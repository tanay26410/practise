#arithmetic subarrays
def arithmetic(nums,l,r):
    # def check(l):
    #     if len(l)<=1:
    #         return True
    #     l.sort()
    #     d=l[1]-l[0]
    #     for i in range(1,len(l)):
    #         if l[i]-l[i-1]!=d:
    #             return False
    #     return True
    # li=[]
    # for i in range(len(l)):
    #     li.append(check(nums[l[i]:r[i]+1]))
    # return li
    res=[]
    for i in range(len(l)):
        te=nums[l[i]:r[i]+1]
        te.sort()
        t=True
        for j in range(1,len(te)):
            d=te[1]-te[0]
            if te[j]-te[j-1]!=d:
                t=False
        if t==False:
            res.append(False)
        else:
            res.append(True)
    return res

nums=[4,6,5,9,3,7]
l=[0,0,2]
r=[2,3,5]
print(arithmetic(nums,l,r))