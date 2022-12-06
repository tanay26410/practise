#fairpass
t=int(input())
for i in range(t):
    li=list(map(int,input().strip().split()))
    n=li[0]
    k=li[1]
    if n<k:
        lar='YES'
    else:
        lar='NO'
    print(lar)