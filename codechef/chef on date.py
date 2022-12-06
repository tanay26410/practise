#chef on date
t=int(input())
for i in range(t):
    n=list(map(int,input().strip().split()))
    if n[0]>=n[1]:
        ot='YES'
    else:
        ot='NO'
    print(ot) 