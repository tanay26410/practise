#beautiful days at the movies
def beautifulDays(i, j, k):
    # Write your code here
    count=0
    for n in range(i,j+1):
        n=str(n)
        if abs(int(n)-int(n[::-1]))%k==0:
            count+=1
    return count
i=20
j=23
k=6
res=beautifulDays(i,j,k)
print(res)