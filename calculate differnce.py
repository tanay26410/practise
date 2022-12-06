#calculate differnce
i,a=map(int,input().split(' '))
z=a-i
if z%2!=0:
    print((z//2)+1)
else:
    print(z//2+i)