#nth root of number using binary search
def root(n,m):
    l=1
    h=m
    eps=1e-6
    while (h-l)>eps:
        mid=(l+h)/2.0
        if (mid**n)<m:
            l=mid
        else:
            h=mid
    print('%6f'%l)
    print('%6f'%pow(m,(1/n)))

n=int(input())
m=int(input())
root(n,m)