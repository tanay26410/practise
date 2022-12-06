#reverse pair 
def reversepair(nums):
    cou=0
    def reveresepairs(l,h):
        nonlocal cou
        if l==h:
            return nums[h]
        mid=l+(h-l) //2
        le=nums[l:mid]
        ri=nums[mid+1:h] 
        lo=0
        ro=0
        while l<len(le):
            if ro>=len(ri) or le[lo]<=2*ri[ro]:
                cou+=ro
                l+=1
            else:
                r+=1
        return list(reveresepairs(le,ri)) 
    reveresepairs(0,len(nums)-1)
    return cou
nums=[1,2,3,2,1]
print(reversepair(nums))       