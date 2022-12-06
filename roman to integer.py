#roman to integer

def romtoin(s):
    c=m=0
    d={'I' : 1,'V': 5,'X' :10,'L':50,'C' : 100,'D' : 500,'M': 1000}
    s=s[::-1]
    for i in s:
        if d[i]<m:
            c-=d[i]
             
        else:
            m=d[i]
            c+=d[i]
                
    return c

s=input()
res=romtoin(s)
print(res)