#grid balance
t=int(input())
for i in range(t):
    n,m=list(map(int,input().strip().split()))
    c=0
    if n==1 and m==1:
        c=n
    if n%2==0 and m%2==0:
        c=0
    if n%2!=0 and m%2!=0:
        c=((m%2)*m+((n%2)*n)-1)

    if n%2==0 and m%2!=0:
        c=((m%2)*n)
    if n%2!=0 and m%2==0:
        c=((n%2)*m)
    print(c)