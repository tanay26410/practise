#eqalize array(arr)
def equzlize(arr):
    c=m=0
    for i in arr:
        if arr.count(i)>m:
            c=i
            m=arr.count(i)
    co=arr.count(c)
    i=0
    while i!=co:
        if c in arr:
            arr.remove(c)
        i+=1
    return len(arr)


ar=[1,2,2,3]
res=equzlize(ar)
print(res)
