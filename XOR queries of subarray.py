#XOR queries of subarray
from re import sub


def subarray(arr,queries):
    res=[0]*len(queries)
    res=list()
    for i in range(len(queries)):
        temp=0
        for j in range(queries[i][0],queries[i][1]+1):
            temp^=arr[j]
        res.append(temp)
    return res
arr = [16]
queries = [[0,0],[0,0],[0,0]]
print(subarray(arr,queries))