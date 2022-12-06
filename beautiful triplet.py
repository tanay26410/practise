#beautiful triplet
from itertools import count


def trip(arr,d):
    res=[]
    n=len(arr)
    count=0
    for i in range(n):
        if arr[i]+(d) in arr:
            index=arr.index(arr[i]+d)
            if arr[index]+d in arr:
                count+=1
    return count
    
arr=[1, 2, 4, 5, 7, 8, 10]
d=3
print(trip(arr,d))