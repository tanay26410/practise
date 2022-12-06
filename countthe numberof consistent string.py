#countthe numberof consistent string
def count(a,w):
    count=0
    for i in w:
        temp=0
        for j in set(i):
            if j not in set(a):
                temp=1
                break
        if temp==0:
            count+=1
    return count

a='ab'
w=['ab','a','b','abb','abbd']
print(count(a,w))
