#subsequnce sum 
def s(i,arr,su,n,res):
    if i==n and res==su:
        print(res)
        return
    res.append(arr[i])
    su+=arr[i]
    s(i+1,arr,su,n,res)
    res.remove(arr[i])
    su-=arr[i]
    s(i+1,arr,su,n,res)

i=0
arr=[1,2,1]
su=2
n=3
res=[]
s(i,arr,su,n,res)
