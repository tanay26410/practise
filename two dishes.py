#two dishes
t=int(input())
for i in range(t):
    n,s=map(int,input().split(','))
    v=abs(int(n)-int(s))
    ans=abs(int(v)-int(n))
    print(ans)
    
    