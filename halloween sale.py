#halloween sale
def halloween(p,d,m,s):
    sum=count=0
    while sum<=s:
        sum+=p
        p=max(p-d,m)
        
        count+=1
    return count-1

p,d,m,s=16,2,1,9981
print(halloween(p,d,m,s))