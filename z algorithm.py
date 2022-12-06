#z algorithm
def zAlgorithm(s, p, n, m):
    h=m
    l=0
    count=0
    while h<=n:
        if p==s[l:h]:
            count+=1
        l+=1
        h+=1
    return count
s=input()
p=input()
n=int(input())
m=int(input())
print(zAlgorithm(s,p,n,m))