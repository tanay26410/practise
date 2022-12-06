#closest number
def clos(arr):
    arr.sort()
    di=[]
    for i in range(1,len(arr)):
        di.append(abs(arr[i]-arr[i-1]))
    val=[]
    for i in range(1,len(arr)):
        if abs(arr[i]-arr[i-1])==min(di):
            val.append(arr[i])
            val.append(arr[i-1])
    val.sort()
    return val
# arr=[-5 ,15 ,25, 71 ,63]
# arr=[5, 4, 3, 2]
arr=[-20 ,-3916237 ,-357920 ,-3620601, 7374819, -7330761 ,30, 6246457 ,-6461594, 266854 ]
print(clos(arr))