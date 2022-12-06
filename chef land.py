#chef land
t=int(input())
for i in range(t):
    a,b,x=map(int,input().split(' '))
    t=int(b)-int(a)
    print(t//int(x))