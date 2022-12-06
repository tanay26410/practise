#longest palindromic 

def longest(s):
    b=[]
    b.extend(s)
    l=[]
    for i in range(len(s)):
        a=b[i]
        if b[i:]==a.sort(reverse=True):
            l.append(b[i])
    return l
s='babad'
res=longest(s)
print(res)