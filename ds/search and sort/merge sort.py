def merge(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    l=arr[:mid]
    r=arr[mid:]
    l=merge(l)
    r=merge(r)
    res=[]
    while len(l)!=0 and len(r)!=0:
        if l[0]<r[0]:
            res.append(l[0])
            l.remove(l[0])
        else:
            res.append(r[0])
            r.remove(r[0])
    if  len(r)==0:
            res+=l
    else:
            res+=r
    return res
arr=[12, 11, 13, 5, 6, 7]
print(merge(arr))