#recursion of subsequence
def subsquence(ind,arr,res,l):  #def subsquence(arr,res,l):
    if ind>=len(arr):           #res.append(l)
        print(res)              #for i in range(len(nums)):
        print(l)                       #subsquence(arr,res,l+[nums[i]])                                            
        return                  #return res
    res.append(arr[ind])
    subsquence(ind+1,arr,res,l)
    res.pop()
    subsquence(ind+1,arr,res,l)
arr=[3,1,2]
res=[]
l=[]
print(subsquence(arr,res,l))