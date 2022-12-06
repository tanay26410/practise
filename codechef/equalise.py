#equalise
T=int(input())
for _ in range(T):
    A,B=list(map(int,input().strip().split()))
    ans='NO'
    if A==B:
        ans='YES'
    elif A>B:
        while A!=B and A>B:
            A/=2
        if A==B:
            ans="YES"
    else:
        while A!=B and A<B:
            B/=2
        if A==B:
            ans='YES'
    print(ans)