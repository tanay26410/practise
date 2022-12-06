#insertion sort 2
def insertionSort2(n, arr):
    # Write your code here
    for i in range(1,n):
        new=arr[i]
        j=i-1
        while j>=0 and new<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=new
        for k in arr:
            print(k,end=' ')
        print()
arr=[1,4,2,5,6]
n=len(arr)
insertionSort2(n,arr)