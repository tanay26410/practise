#chef programming lanng
t=int(input())
for i in range(t):
    n=list(map(int,input().strip().split()))
    a=n[2:4]
    b=n[4:]
    c=n[:2]
    a.sort()
    b.sort()
    c.sort()
    if c==a:
        print(1)
    elif c==b:
        print(2)
    else:
        print(0)