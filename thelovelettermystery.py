#thelovelettermystery

def loveletter(q):
    count=0
    li=[]
    for i in range(0,len(q)//2):
        if q[i]!=q[-(i+1)]:
            li.append(abs(ord(q[i])-ord(q[-(i+1)])))
    return sum(li)
q='abcd'
print(loveletter(q))