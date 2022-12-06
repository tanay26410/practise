def stringAndSubset(s,n,ra):
	r = [[]]
	for i in range(n):
		for j in range(n):
			b = s[i:j+1]
			if b:
				r.append(b)
	res = sorted(r, key=lambda x:len(x))[ra-1]
	for i in range(len(res)):
		if i != len(res)-1:
			print(res[i],end=",")
		else:
			print(res[i])
n = int(input())
ra = int(input())
st = list(map(str, input().split(',')))
stringAndSubset(st,n,ra)