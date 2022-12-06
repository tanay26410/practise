#minimum absolete differen
from re import A


def diff(arr):
    mi=max(arr)
    arr.sort()
    for i in range(len(arr)-1):
                mi=min(abs(arr[i]-arr[i+1]),mi)
    return mi      



t=int(input())
arr=list(map(int,input().strip().split()))
print(diff(arr))