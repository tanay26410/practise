#combination sum
def rec(ind,candidates,target,ans,ds):
        
        if target==0:
                ans.append(ds)
                return
        
        if candidates[ind]<=target:
            for i in range(ind,len(candidates)):
                rec(i,candidates,target-candidates[i],ans,ds+[candidates[i]])
def combinationSum(candidates,target):
        ds=[]
        ans=[]
        candidates.sort()
        rec(0,candidates,target,ans,ds)
        return ans
arr=[2,3,6,7]
t=7
print(combinationSum(arr,t))