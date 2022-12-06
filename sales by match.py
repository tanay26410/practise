#sales by match
def sock(n,ar):
    d={}
    count=0
    r=0
    for i in range(n):
         d[ar[i]]=ar.count(ar[i])
    for i in d.values():
        if i>1 :
            r=i//2
            count+=r
    return count

ar= [10, 20, 20, 10, 10, 30, 50, 10, 20]
n=9
res=sock(n,ar)
print(res)