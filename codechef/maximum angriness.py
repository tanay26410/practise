t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    res=(n*(n-1))//2
    if n==1:
        print(0)
    else:

        if k>=n//2:
            print(res)
        elif n//2>k:
            x=n-2*k
            t=res-(x*(x-1))//2
            print(t)