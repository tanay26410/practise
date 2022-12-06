#Minimum Distances
from re import L


def minimun(a):
    l=0
    r=len(a)-1
    mi=[]
    while l<=r:
        if a[l]==a[r]:
            mi.append(r-l)
        l+=1
        r-=1
    if min(mi)==0:
        return -1
    return min(mi)

            

# arr = [7, 1, 3, 4, 1, 7]
arr=[1, 2, 3 ,4 ,10]
print(minimun(arr))