#recursion reverse
def rev(arr,l,r): #rev(arr,i)
    if l>=r: #i>=len(arr)//2
        print(arr)
        return arr
    arr[l],arr[r]=arr[r],arr[l] #arr[i]=arr[n-i-1]
    
    rev(arr,l+1,r-1)#rev(arr,i+1)
arr=[2,4,5,1,6,7,8]
l=0
r=len(arr)-1
print(rev(arr,l,r))#print(rev(arr,l))