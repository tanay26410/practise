#mark and toys
def maximum(prices,k):
    b=count=0
    prices.sort()
    for i in prices:
        if b+i<=k:
            count+=1
            b+=i
    return count
prices=[1,2,3,4]
k=7
print(maximum(prices,k))