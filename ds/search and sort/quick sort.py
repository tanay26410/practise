#quick sort
def quick(arr,l,h):
    i=l-1
    pi=arr[h]
    for j in range(l,h):
        if arr[j]<=pi:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1
def quicksort(arr,l,h):
    if len(arr)==1:
        return arr
    if l<h:
        pi=quick(arr,l,h)
        quicksort(arr,l,pi-1)
        quicksort(arr,pi+1,h)
    return arr
arr=[10, 7, 8, 9, 1, 5]
n=len(arr)
quicksort(arr,0,n-1)
print(arr)