#twotrains
T=int(input())
for i in range(T):
    n=int(input())
    t=list(map(int,input().strip().split()))[:n-1]
    print(sum(t)+max(t))