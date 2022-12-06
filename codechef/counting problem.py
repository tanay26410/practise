#counting problem
t=int(input())
for i in range(t):
    n=int(input())
    res=''
    a=list(map(int,input().split()))
    e,o=0,0
    for i in a:
        if i%2==0:
            e+=1
        else:
            o+=1
    if o%2==0 and o!=0:
        res='YES'
    else:
        res='NO'
    print(res)