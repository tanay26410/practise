#bidding
T=int(input())
for i in range(T):
    s=list(map(int,input().strip().split()))
    ind=s.index(max(s))
    if ind==0:
        l='Alice'
    elif ind==1:
        l='Bob'
    else:
        l='Charlie'
    print(l)
    
        
