#kaprekarnumber
def kaprekar(p,q):
    d={}
    for i in range(p,q+1):
        d[i]=str(i**2)
    li=[]
    res=[]
    for i in d.values():
        if len(i)==1:
            li.append(int(i))
        else:
            x=len(i)//2
            li.append(int(i[:x])+int(i[x:]))
    for i,j in zip(li,d.keys()):
        if i==j:
            res.append(i)
    return res

p=1
q=99999
print(kaprekar(p,q))
        