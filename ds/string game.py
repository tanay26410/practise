#string game
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    a,b='',''
    s=[i for i in s]
    if n%2==1:
        print('NO')
    elif len(set(s))==n:
        print('NO')
    else:
        
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        s=set()
        for i in d.values():
            s.add(i)
        if len(s)==1:
            print('yes')
        else:
            print('no')