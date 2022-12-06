#icecream palor
def icecream(m,arr):
    indices=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[i]+arr[j])==m:
                return i+1,j+1
arr=[2,2,4,3]
k=4
print(icecream(k,arr))