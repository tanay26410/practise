#expense list
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    mi=2**b
    res=0
    for i in range(a):
        res=mi-mi//2
        mi=mi//2
    print(res)