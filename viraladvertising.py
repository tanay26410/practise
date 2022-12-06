#viraladvertising
from re import L


def viraladvertising(n):
    l=[]
    for i in range(1,n+1):
        if i==1:
            l.append(5)
        else:
            a=max(l)//2
            l.append(a*3)
    c=0
    for i in l:
        c+=i//2
    return c



n=5
res=viraladvertising(n)
print(res)