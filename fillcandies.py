#fillcandies
t=int(input())
for i in range(t):
    n,k,m=list(map(int,input().strip().split()))
    c=0
    if n%(m*k)!=0:
        c=n//(m*k)+1
    else:
        c=n//(m*k)
    print(c)