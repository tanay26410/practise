#common child
def commonChild(s1, s2):
    # Write your code here
    l=[]
    l.extend(s1)
    b=[]
    b.extend(s2)
    a=set(l)
    c=set(b)
    return(len(a.intersection(b)))    
s1='abcdef'
s2='fbdamn'
res=commonChild(s1,s2)
print(res)