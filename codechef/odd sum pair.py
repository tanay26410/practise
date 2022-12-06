#odd sum pair
n=int(input())
res=''
for _ in range(n):
    li=list(map(int,input().split()))
    a,s,d=li
    if a+s&1 or (a+d&1 and s+d&1):
        print('YES')
    else:
        print('NO')