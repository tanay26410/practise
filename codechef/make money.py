#make money
# cook your dish here
t=int(input())
for _ in range(t):
    n,x,cost=map(int,input().split())
    c=0
    a=list(map(int,input().split()))
    for i in range(n):
        if x-a[i]>cost:
            a[i]=x
            c+=cost
    sum=0
    for i in range(n):
        sum+=a[i]
    print(sum-c)
                