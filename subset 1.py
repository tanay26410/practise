#subset 1
def rec(res,ds,arr):
    res.append(ds)
    for i in range(len(arr)):
        rec(res,ds+[arr[i]],arr[i+1:])

def subset(arr):
    res=ds=[]
    rec(res,ds,arr)
    return res
arr=[3,1,2]
print(subset(arr))