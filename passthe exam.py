#passthe exam
t=int(input())
for i in range(t):
    s=list(map(int,input().strip().split()))
    m=min(s)
    su=sum(s)
    if su>=100 and  m>=10:
        print('PASS')
    else:print('FAIL')