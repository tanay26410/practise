#permutation sequence
def getpermu(n,k):
    arr=[i for i in range(1,n+1)]
    ans=''
    while n>0:
        a=1
        for i in range(1,n):
            print('i',i)
            a*=i
            print('a',a)
        c=(k-1)//a
        print('c',c)
        ans=str(arr.pop(c))
        print('ans',ans)
        k-=c*a
        print('k',k)
        print('  \n')
        n-=1
    return ans
n=3
k=3
print(getpermu(n,k))
