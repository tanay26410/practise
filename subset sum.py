#subset sum
def solve(x,arr,l,n,su):
    if x==n:
        l.append(su)
        return
    solve(x+1,arr,l,n,su+arr[x])
    solve(x+1,arr,l,n,su)
def subsetsum(arr,N):
    l=[]
    solve(0,arr,l,N,0)
    return l
arr=[2,3]
N=2
print(subsetsum(arr,N))