# concatenation ques1
def conca(a):
    b=a.index(5)
    c=a.index(8)
    su=0
    su1=0
    for i in a[0:b]:
        su+=i
    for i in a[c+1:]:
        su1+=i
    return su1+su
l1=[1,2,3,4,5,6,7,8]
print(conca(l1))