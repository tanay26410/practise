#endsort
t=int(input())
for i in range(t):
    count=0
    n=input()
    n=int(n)
    a=b=0
    li=list(map(int,input().strip().split()))[:n]
    for j in range(n):
        if li[j]==1:
            a=j
        if li[j]==n:
            b=j
    if a<b:
            print((n-1)+(a-b))
    else:
            print(a-b+n-2)
             