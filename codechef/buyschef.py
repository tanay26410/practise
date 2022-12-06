#buylamps
t=int(input())
for i in range(t):
    n,k,x,y=list(map(int,input().strip().split()))
    c=0
    if x<y:
        c=n*x
    else:
        b=n-k
        c=(k*x)+(b*y)
    print(c)