#gamewithstring
from collections import defaultdict


def game(s,k):
    
    su=0
    d=defaultdict(int)
    for i in s:
        d[i]+=1
    f=list(d.values())
    f.sort(reverse=True)
    while k!=0:
        f[0]=f[0]-1
        f.sort(reverse=True)
        k-=1
    for i in f:
        su+=i*i
    return su
s=input()
k=int(input())
print(game(s,k))
 