
def maxProfit(val, wt, n, w):
    dp=[[-1 for i in range(w+1)]for j in range(n+1)]
    def f(wt,val,ind,w,dp):
        if ind == 0:
            if wt[ind] <= w:
                return val[0]
            else:
                return 0
        if dp [ind] [w] != -1:
            return dp [ind] [w]
        nottake = 0 + f(wt , val , ind-1 , w , dp)
        take = float('-inf')
        if wt [ind] <= w:
            take = val[ind] + f ( wt , val , ind-1 , w - wt[ind] , dp)
        dp [ind] [w] = max( take , nottake )
        return dp [ind] [w]
    return f(wt , val , n-1 ,w , dp)