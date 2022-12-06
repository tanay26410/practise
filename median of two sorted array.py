#median of two sorted array
def findmedian(nums1,nums2):
    li=nums1+nums2
    li.sort()
    n=len(li)
    if n%2!=0:
        return li[n//2]
    else:
        return (li[n//2]+li[(n//2)-1])/2


nums1=[1,3]
nums2=[2,4]
print(findmedian(nums1,nums2))