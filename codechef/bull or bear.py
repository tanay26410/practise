#bull or bear
t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    res=''
    if a>b:
        res='LOSS'
    elif a==b:
        res='NEUTRAL'
    else:
        res='PROFIT'
    print(res)