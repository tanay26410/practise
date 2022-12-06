#missing number
from unittest import result


def missing(arr,brr):
    l=[]
    c=0
    c1=0
    for i in set(brr):
        c=arr.count(i)
        c1=brr.count(i)
        if c1>c:
            l.append(i)
    return l


arr=[7,2,5,3,5,3]
brr=[7,2,5,4,6,5,3]
resu=missing(arr,brr)
print(resu)
