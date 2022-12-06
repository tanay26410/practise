import math
def m(arr,k):
    wstart=0
    maxsum=1
    wsum=0
    wend=0
    for wend in range(len(arr)-1):
        wsum=wsum+arr[wend]
        if(wend-wstart+1==k):
            maxsum=m(maxsum,wsum)
        wsum=wsum-arr(wstart)
        wstart+=1
Arr=[2,3,4,5,6]
k1=2
res=m(Arr,k1)
print(res)
