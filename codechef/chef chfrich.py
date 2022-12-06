#chef chfrich
t=int(input())
for i in range(t):
    n=list(map(int,input().strip().split()))
    diff=n[1]-n[0]
    res=diff//n[-1]
    print(res)