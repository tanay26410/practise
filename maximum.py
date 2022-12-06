#maximum
from re import L


def bitwise(arr):
    arr.remove(arr[0])
    l=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            l.append(arr[i]*arr[j])
    l.sort()
    return l
    
N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))
print(bitwise(arr))