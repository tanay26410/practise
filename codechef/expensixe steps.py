#xpensixe steps
#counting problem
t=int(input())
for i in range(t):
    li=list(map(int,input().split()))
    def func(li):
        n,x1,y1,x2,y2=li
        if x1<1 and y1>n and x2<1 and y2>n:
            return 0
        elif(x1<1 or y1>n):
            return min(min(n-x2+1,n-y2+1),min(x2,y2))
        elif x2<1 or y2>n:
            return min(min(n-x1+1,n-y1+1),min(x1,y1))
        x=min(min(n-x1+1,n-y1+1),min(x1,y1))
        y=min(min(n-x2+1,n-y2+1),min(x2,y2))
        z=abs(x1-x2)+abs(y1-y2)
        return min(z,x+y)
    print(func(li))
    