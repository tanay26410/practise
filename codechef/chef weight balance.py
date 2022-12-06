#chef weight balance
t=int(input())
for i in range(t):
    n=list(map(int,input().strip().split()))
    x1=n[2]*n[-1]
    x2=n[3]*n[-1]
    if x1<=n[1]-n[0] and x2>=n[1]-n[0]:
        print(1)
    else:
        print(0)     