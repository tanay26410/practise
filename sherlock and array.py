#sherlock and array
def balancedSums(arr):
    count=0
    z=0
    l2=sum(arr[1:])
    for i in range(len(arr)):
        if i == 0:
            if 0==l2:
                count+=1
                break
        else:
            z=z+arr[i-1]
            l2-=arr[i]
            if z==l2:
                count+=1
                break        
    if count>0:
        return 'YES'
    return 'NO'
arr=[1 ,2 ,3]
res=balancedSums(arr)
print(res)