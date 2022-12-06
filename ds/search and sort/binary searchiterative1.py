def binarysearchiterative(arr,x,l,h):
    while (l <= h):
        m = l + (h-l)//2
        if arr[m] == x: 
            return m
        elif arr[m] < x: 
            l = m + 1 
        else :
            h = m - 1
    return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binarysearchiterative(arr,x, 0, len(arr)-1)
if result!=-1:
    print(str(result))
else:
    print("not found")