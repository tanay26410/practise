#indices
from errno import E2BIG
from hashlib import sha3_224


def indices(arr,i,j,k,n):
    e1=arr[0:i+1]
    e2=arr[i+1:j+1]
    e3=arr[j+1:k+1]
    e4=arr[k:n-1]
    s1=sum(e1)
    s2=sum(e2)
    s3=sum(e3)
    s4=sum(e4)
    ma=max(s1,s2,s3,s4)
    mi=min(s1,s2,s3,s4)
    
    return e4
n=6
arr=[1,2,3,4,3,2,1]
i=1
j=2
k=3
print(indices(arr,i,j,k,n))