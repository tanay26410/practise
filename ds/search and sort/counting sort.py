#counting sort
from operator import countOf


def counting(arr,n):
    out=[0]*n
    a=max(arr)+1
    cou=[0]*a
    for i in arr:
        cou[i]+=1
    for j in range(1,a):
        cou[j]+=cou[j-1]
    for  i in range(n-1,-1,-1):
        out[cou[arr[i]]-1]=arr[i]
        cou[arr[i]]-=1

    return out
    
arr=[4, 2, 2, 8, 3, 3, 1]
n=len(arr)
print(counting(arr,n))