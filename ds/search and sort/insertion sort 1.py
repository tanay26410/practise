#insertion sort 1
def insertionSort1(n, arr):
    # Write your code her
    for i in range(1, n):
                key = arr[i]
                j = i-1
                while j >= 0 and key < arr[j] :
                        arr[j + 1] = arr[j]
                        j -= 1
                        for k in range(n):
                            print(arr[k],end=' ')
                        print()
                arr[j + 1] = key
    for k in range(n):
            print(arr[k],end=' ')
arr=[2, 4, 6, 8, 3]
n=len(arr)
insertionSort1(n,arr)