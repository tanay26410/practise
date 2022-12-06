#ravi
N=int(input())
l=[]
for i in range(N):

    temp=int(input())
    l.append(temp)
Q=int(input())
q=[]
for i in range(Q):
    tem=int(input())
    q.append(tem)
for b in q:
    print(sum(l[:b]))
