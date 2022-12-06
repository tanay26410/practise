#hello equation
t=int(input())
for _ in range(t):
    x=int(input())
    s=0
    for i in range(1,int(x**.5)):
        if (x-2*i)%(i+2)==0 and x!=2*i:
            s=s+1
            break
    if s==0:
        print('NO')
    else:
        print('YES')