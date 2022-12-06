#pairs
def pairs(k,arr):
    count=0
    arr.sort()
    arr=set(arr)
    l=[]
    for i in arr:
            if i-k in arr:
                count+=1   
    return count
arr=[1,3,5,8,6,4,2]
k=2
res=pairs(k,arr)
print(res)