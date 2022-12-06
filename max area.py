#max area
def maxarea(a):
    l=0
    r=len(a)-1
    area=0
    while l<r:
        area=max(area,a[r]-a[l])
        if a[l]<a[r]:
            r-=1
        else:
            l+=1
    
    return area
# height=[1,8,6,2,5,4,8,3,7]
height=[2,1,4]
# height=[7,1,5,3,6,4]
print(maxarea(height))