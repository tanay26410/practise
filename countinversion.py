#countinversion
def inversion(arr,n):
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                count+=1
    return count



# arr,n=[2,5,1,3,4],5
arr,n=[3,2,1],3
print(inversion(arr,n))