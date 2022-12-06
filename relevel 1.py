#relevel 1
T=int(input())
for i in range(T):
	n=int(input())
	count=0
	a=list(map(int,input().strip().split()))
	while len(set(a))!=len(a):
		mx=max(a)
		a.remove(mx)
		a=[i-mx for i in a]
		count+=1
	print(count,end=" ")
	print(min(a))