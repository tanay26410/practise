#chef vdates
t=int(input())
for i in range(t):
    D,L,R=list(map(int,input().strip().split()))
    if L<=D and D<=R:
        out='Take second dose now'
    elif D>=R:
        out="Too Late"
    else:
        out='Too Early'
    print(out)
