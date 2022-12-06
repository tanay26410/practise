# electronics shop
def getmoney(k,d,b):
    l=[]
    m=-1
    for i in k:
        for j in d:
            if i+j<=b:
                c=i+j
                if c>m:
                    m=c
    return m  
k=[3,1]
d=[5,2,8]
b=10
res=getmoney(k,d,b)
print(res)