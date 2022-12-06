#appendanddelete
def append(s,t,k):
    if len(s)+len(t)<k:return 'Yes'
    count=0
    for i,j in zip(s,t):
        if i==j:
            count+=1
        else:   
            break
    s_=len(s)-count
    t_=len(t)-count
    d=s_+t_
    if d<=k and d%2==k%2:
        return 'Yes'
    return'No'
s='aaa'
t='a'
k=5
res=append(s,t,k)
print(res)
