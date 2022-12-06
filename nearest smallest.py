#nearest smallest element:
def ns(arr):
    res=[-1]*len(arr)
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                res[i]=arr[j]
                break
        else: res[i]=-1
    return res
n=list(map(int,input().strip().split()))
print(ns(n))